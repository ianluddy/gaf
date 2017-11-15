SESSION_DURATION_SECONDS = 24000000  # TODO reset this to 2400
API_AUTH_ENABLED = False # TODO re-enable this
GOOGLE_API_KEY = "AIzaSyC5WVwaakrs8CzWJZEhUl3cByp0T4FBOo0"

PROPERTY_TYPES = {
    1: "Entire Property",
    2: "Room",
    3: "Digs"
}

USER_TYPES = {
    1: "Tenant",
    2: "Landlord/Agent",
    3: "Student Swap"
}

PROVINCES = {
    1: "Connacht",
    2: "Leinster",
    3: "Munster",
    4: "Ulster"
}

COUNTIES = {
    1: "Antrim",
    2: "Armagh",
    3: "Carlow",
    4: "Cavan",
    5: "Clare",
    6: "Cork",
    7: "Derry",
    8: "Donegal",
    9: "Down",
    10: "Dublin",
    11: "Fermanagh",
    12: "Galway",
    13: "Kerry",
    14: "Kildare",
    15: "Kilkenny",
    16: "Laois",
    17: "Leitrim",
    18: "Limerick",
    19: "Longford",
    20: "Louth",
    21: "Mayo",
    22: "Meath",
    23: "Monaghan",
    24: "Offaly",
    25: "Roscommon",
    26: "Sligo",
    27: "Tipperary",
    28: "Tyrone",
    29: "Waterford",
    30: "Westmeath",
    31: "Wexford",
    32: "Wicklow"
}

PROVINCE_COUNTIES = {
    1: [12, 21, 26, 17, 25],
    2: [3, 10, 14, 15, 16, 19, 20, 22, 24, 30, 31, 32],
    3: [5, 6, 13, 18, 27, 29],
    4: [1, 2, 4, 7, 8, 9, 11, 23, 28]
}

# Strings

NOT_AUTH = "You dont have permission"
EMAIL_NOT_FOUND = "Email address not registered"
EMAIL_ADDRESS_TAKEN = "Email address already registered"
PASSWORD_DOESNT_MATCH = "Password doesn't match"
PASSWORD_NOT_VALID = "Password should be at least 8 characters long"
EMAIL_NOT_VALID = "Email address not valid"
SESSION_EXPIRED = "Please login to view this page"
PHOTO_UPDATED = "Photo Updated"
CONTRACT_ADDED = "Contract Added"
CONTRACT_UPDATED = "Contract Updated"
CONTRACT_CANCELLED = "Contract Cancelled"
MESSAGE_ADDED = "Message Added"
MESSAGE_UPDATED = "Message Updated"
MESSAGE_DELETED = "Message Deleted"
FEEDBACK_ADDED = "Feedback Added"
FEEDBACK_UPDATED = "Feedback Updated"
FEEDBACK_DELETED = "Feedback Deleted"
LISTING_ADDED = "Listing Added"
LISTING_DELETED = "Listing Removed"
LISTING_UPDATED = "Listing Updated"
ACCOUNT_CREATED = "Account Created"
LOGGED_OUT = "Logged Out"
LOGGED_IN = "Logged In"
PASSWORD_CHANGED = "Password Changed"
PROFILE_UPDATED = "Profile Updated"
ADDED = "Added"
UPDATED = "Updated"
REMOVED = "Removed"
