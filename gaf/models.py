from gaf.core import db
from gaf import app
from datetime import datetime

# TODO - add indexes

class BaseModel:

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def to_dict(self):
        output = self.__dict__
        del output['_sa_instance_state']
        return output

class StampedModel(BaseModel):

    created = db.Column(db.DateTime, nullable=False, default=datetime.now())

class Listing(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    description = db.Column(db.String)
    address1 = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    postcode = db.Column(db.String)
    image = db.Column(db.String, default="", nullable=False)
    images = db.Column(db.String, default="", nullable=False)
    lender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    published = db.Column(db.Boolean, default=False, nullable=False)
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'))
    county = db.relationship('County')
    province_id = db.Column(db.Integer, db.ForeignKey('province.id'))
    province = db.relationship('Province')
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def to_dict(self):
        # TODO - implement similar call with less info for search results page
        county = self.county.name if self.county else None
        off_days = [day.id for day in self.days]
        output = super(Item, self).to_dict()
        output['county'] = county
        del output['days']
        output['off_days'] = off_days
        return output

class County(db.Model, BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey('province.id'), nullable=False)
    province = db.relationship('Province', backref="counties")
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

class Province(db.Model, BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def to_dict(self):
        counties = [county.to_dict() for county in self.counties]
        output = super(Province, self).to_dict()
        output['counties'] = counties
        return output

class Message(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String, nullable=False)

class Category(db.Model, BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    count = db.Column(db.Integer, nullable=False, default=0)
    image = db.Column(db.String, nullable=False, default="todo") # TODO

class User(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String, nullable=False)
    last = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    phone = db.Column(db.String)
    dob = db.Column(db.DateTime)
    email_verified = db.Column(db.Boolean, nullable=False, default=False)
    phone_verified = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String, nullable=False) # TODO - encrypt
    intro = db.Column(db.String)

    def to_dict(self):
        output = super(User, self).to_dict()
        del output['password']
        return output
