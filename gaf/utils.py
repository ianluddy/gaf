# import gpxpy.geo
import json
import os
import uuid

from flask import request

"""
def geoDistance(lat1, lng1, lat2, lng2):
    return gpxpy.geo.haversine_distance(lat1, lng1, lat2, lng2)

def geoDistanceString(dist):
    if dist > 1000:
        return str(int(dist / 1000)) + "km"
    return "~" + str(int(dist)) + "m"
"""

def generate_uuid():
    return str(uuid.uuid4())

def store_file(file, path):
    extension = file.filename.split('.')[1]
    name = generate_uuid() + "." + extension
    file.save(os.path.join(path, name))
    return name

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
