from database import *
from constants import *
from flask import session
from email.utils import parseaddr

class ApiException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class Service(object):

    model_wrapper = None

    def get(self, key=None, field='id', many=False):
        if key is not None:
            if many:
                return self.model_wrapper.get_many(key, field)
            return self.model_wrapper.get_one(key, field)
        return self.model_wrapper.get_all()

    def post(self, model):
        return self.model_wrapper.post(model)

    def patch(self, model):
        return self.model_wrapper.patch(model)

    def delete(self, id):
        return self.model_wrapper.delete(id)

class SearchService(Service):

    def search(self, id=None, search=None, page=None):
        if search:
            return self.model_wrapper.search(search, page)
        return super(SearchService, self).get(id)

class ListingService(SearchService):
    model_wrapper = PropertyWrapper()

class UserService(Service):
    model_wrapper = UserWrapper()

    def get(self):
        return super(UserService, self).get(session['user_id'])

    def patch(self, input):
        input['id'] = session['user_id'] # Can only patch the logged in user

        # Validate email address if it's being changed
        if 'email' in input:
            email = input['email']
            if email != session['email']:
                self._verify_email_valid(email)
                self._verify_email_available(email)
                session['email'] = email

        super(UserService, self).patch(input)

        if 'image' in input:
            session['image'] = input['image']

    def register(self, input):
        self._verify_email_available(input['email'])
        self._verify_email_valid(input['email'])
        self._verify_password_valid(input['password'])
        self.model_wrapper.post(input)
        self.login(input)

    def login(self, input):
        self._verify_email_exists(input['email'])
        self._verify_password_match(input['email'], input['password'])
        self._start_session(input['email'])

    def logout(self):
        self._end_session()

    def change_password(self, input):
        user = self.model_wrapper.get_one(session['user_id'])
        self._verify_password_match(user['email'], input['current'])
        self._verify_password_valid(input['new'])
        self.model_wrapper.set_password(session['user_id'], input['new'])

    def get_session(self):
        return session

    def _start_session(self, email):
        user = self.model_wrapper.get_one(email, 'email')
        session['user_id'] = user['id']
        session['user_first'] = user['first']
        session['user_last'] = user['last']
        session['email'] = user['email']
        session['image'] = user['image']

    def _end_session(self):
        # TODO - expire sessions
        session.clear()

    def _verify_email_exists(self, email):
        if self.model_wrapper.get_one(email, field='email') is None:
            raise ApiException(EMAIL_NOT_FOUND, status_code=400)

    @staticmethod
    def _verify_password_valid(password):
        if password is None or len(password) < 8:
            raise ApiException(PASSWORD_NOT_VALID, status_code=400)

    @staticmethod
    def _verify_email_valid(email):
        parsed = parseaddr(email) if email else None
        if parsed is None or '@' not in parsed[1] or '.' not in parsed[1]:
            raise ApiException(EMAIL_NOT_VALID, status_code=400)

    def _verify_email_available(self, email):
        if self.model_wrapper.get_one(email, field='email') is not None:
            raise ApiException(EMAIL_ADDRESS_TAKEN, status_code=400)

    def _verify_password_match(self, email, password):
        if not self.model_wrapper.get_password(email) == password:
            raise ApiException(PASSWORD_DOESNT_MATCH, status_code=400)
