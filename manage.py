import json
import argparse
import requests
from gaf.core import db

seed_order = ['user']

def create_sample_db_entry(api_endpoint, payload):
    url = 'http://localhost:5000/' + api_endpoint
    r = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if r.status_code != 200:
        print r.text

def create_db():
    db.create_all()

def drop_db():
    db.drop_all()

def seed_db(seedFile):
    drop_db()
    create_db()
    with open(seedFile, 'r') as f:
        seed_data = json.loads(f.read())

    for item_class in seed_order:
        items = seed_data[item_class]
        for item in items:
            create_sample_db_entry('api/' + item_class, item)
        print item_class + " -- Done"

    print "\nSample data added to database!"

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

    elif args.command == 'seed_db' and args.seedfile:
        seed_db(args.seedfile)

    else:
        raise Exception('Invalid command')

if __name__ == '__main__':
    main()
