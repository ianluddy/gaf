import os
from functools import wraps

import flask
from flask import jsonify, session, redirect, url_for
from flask import render_template, send_from_directory

from gaf.constants import *
from gaf import app

from services import ApiException
from services import PropertyService, UserService


### Helpers ###

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if API_AUTH_ENABLED and 'user_id' not in session:
            raise ApiException('Please login to continue', 401)
        return f(*args, **kwargs)
    return decorated_function

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

def render(template):
    return render_template(template, **{'session': user_service.get_session()})

### Services ###

user_service = UserService()
listing_service = PropertyService()

### Pages ###

@app.route('/')
def index():
    return render('index.html')

@app.route('/contact')
def contact():
    return render('contact.html')

@app.route('/about')
def about():
    return render('about.html')

@app.route('/agents')
def agents():
    return render('agents.html')

@app.route('/register')
def register():
    return render('register.html')

@app.route('/signin')
def signin():
    return render('signin.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
