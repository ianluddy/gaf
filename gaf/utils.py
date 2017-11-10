# import gpxpy.geo
import uuid
import os
from gaf.constants import *

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
