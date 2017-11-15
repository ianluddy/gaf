from gaf.core import db
from gaf import app
from datetime import datetime
from gaf.core import api_manager

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

class Property(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    type = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    address1 = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    postcode = db.Column(db.String)
    image = db.Column(db.String, default="", nullable=False)
    images = db.Column(db.String, default="", nullable=False)
    landlord_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    published = db.Column(db.Boolean, default=False, nullable=False)
    county_id = db.Column(db.Integer, nullable=False)
    province_id = db.Column(db.Integer, nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

class UserReview(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class PropertyReview(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.String, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Conversation(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    read = db.Column(db.Boolean, default=False)

class Message(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)
    read = db.Column(db.Boolean, default=False)

class Notification(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    read = db.Column(db.Boolean, default=False)

class User(db.Model, StampedModel):

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False)
    first = db.Column(db.String, nullable=False)
    last = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    phone = db.Column(db.String)
    dob = db.Column(db.DateTime)
    email_verified = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String, nullable=False) # TODO - encrypt
    intro = db.Column(db.String)


    def to_dict(self):
        output = super(User, self).to_dict()
        del output['password']
        return output

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
for model in [
    User,
    Property,
    UserReview,
    PropertyReview,
    Message,
    Notification,
    Conversation
]:
    api_manager.create_api(model, methods=['GET', 'POST', 'DELETE', 'PATCH'])