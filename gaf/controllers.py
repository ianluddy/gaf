import os
import flask
import json
from flask import render_template, send_from_directory
from flask import jsonify, session, request, redirect, url_for
from services import UserService, ListingService
from services import ApiException
from gaf.models import *
from gaf.constants import *

from functools import wraps

### Decorators ###

def parse_args(method='post', string_args=None, int_args=None, float_args=None, json_args=None, bool_args=None, datetime_args=None):
    def actualDecorator(test_func):
        @wraps(test_func)
        def wrapper(*args, **kwargs):

            if method == 'get':
                input = request.args
            elif request.data:
                input = json.loads(request.data)
            else:
                input = {}

            output = {}
            if string_args:
                for key in string_args:
                    if key in input:
                        output[key] = input[key]

            if int_args:
                for key in int_args:
                    if key in input:
                        output[key] = int(input[key]) if input[key] is not None else None

            if float_args:
                for key in float_args:
                    if key in input:
                        output[key] = float(input[key]) if input[key] is not None else None

            if bool_args:
                for key in bool_args:
                    if key in input:
                        output[key] = bool(input[key]) if input[key] is not None else None

            if json_args:
                for key in json_args:
                    if input.get(key):
                        output[key] = input[key]

            if datetime_args:
                for key in datetime_args:
                    if input.get(key):
                        output[key] = datetime.strptime(input[key], '%d-%m-%y')

            return test_func(output, *args, **kwargs)
        return wrapper
    return actualDecorator

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if API_AUTH_ENABLED and 'user_id' not in session:
            raise ApiException('Please login to continue', 401)
        return f(*args, **kwargs)
    return decorated_function

### Handlers ###

@app.errorhandler(ApiException)
def handle_api_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.before_request
def check_session():
    session.permanent = True

def validate_session():
    if API_AUTH_ENABLED and 'user_id' not in session:
        return redirect(url_for('root'))

def response(**output):
    if "status" not in output:
        output['status'] = 200
    return flask.jsonify(**output)

### Services ###

user_service = UserService()
listing_service = ListingService()

### Pages ###

@app.route('/')
def root():
    return render_template('index.html', **{'session': user_service.get_session()})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
