import json
import argparse
import requests
from random import choice
from datetime import datetime
from gaf.constants import LOREM
from gaf.core import db

def create_sample_db_entry(api_endpoint, payload):
    url = 'http://localhost:5000/' + api_endpoint
    r = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if r.status_code != 200:
        print r.text

def create_db():
    db.create_all()

def drop_db():
    db.drop_all()

def seed_db():
    drop_db()
    create_db()

    seedlist = [
        {
            'type': 'user',
            'count': 100,
            'func': new_user
        },
        #{
        #    'type': 'property',
        #    'count': 100,
        #    'func': new_property
        #},
    ]

    for item in seedlist:
        id = 0
        for i in range(item['count']):
            create_sample_db_entry('api/' + item['type'], item['func'](id))
            id += 1
        print item['type'] + " done"

    print "\nDB Seeded"

def new_user(id):
    return {
        "first": choice(["Joe", "Jane", "Jill", "Jack", "John", "James", "Joanna"]),
        "last": choice(["Murphy", "O'Connell", "Luddy", "Cronin", "McDonald", "Joyce", "O'Hara"]),
        "type": choice([1, 2, 3]),
        "email": "user%s@gmail.com" % str(id),
        "password": "password",
        "intro": LOREM,
        "dob": str(datetime.now()),
        "phone": "01-387634876"
    }

def new_property(id):
    return {
        "first": choice(["Joe", "Jane", "Jill", "Jack", "John", "James", "Joanna"]),
        "last": choice(["Murphy", "O'Connell", "Luddy", "Cronin", "McDonald", "Joyce", "O'Hara"]),
        "type": choice([1, 2, 3]),
        "email": "user%s@gmail.com" % str(id),
        "password": "password",
        "intro": LOREM,
        "dob": str(datetime.now()),
        "phone": "01-387634876"
    }

def main():
    parser = argparse.ArgumentParser(
        description='Manage this Flask application.')
    parser.add_argument(
        'command', help='the name of the command you want to run')
    parser.add_argument(
        '--seedfile', help='the file with data for seeding the database')
    args = parser.parse_args()

    if args.command == 'create_db':
        create_db()
        print "DB created!"

    elif args.command == 'drop_db':
        drop_db()
        print "DB deleted!"

    elif args.command == 'seed_db':
        seed_db()

    else:
        raise Exception('Invalid command')

if __name__ == '__main__':
    main()
