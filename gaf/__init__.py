from datetime import timedelta
from flask import Flask
from gaf.constants import SESSION_DURATION_SECONDS

app = Flask(__name__)

app.config.from_object('gaf.settings')

app.url_map.strict_slashes = False

app.permanent_session_lifetime = timedelta(seconds=SESSION_DURATION_SECONDS)

import gaf.core
import gaf.models
import gaf.controllers
import gaf.utils
