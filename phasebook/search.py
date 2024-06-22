from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    # Return default data if no parameters
    if not args:
        return USERS
    
    return [user for user in USERS if filter_users(user, args)]

def filter_users(user, args):
    if 'id' in args and args['id'] != '' and args['id'] == user['id']:
        return True
    
    if 'name' in args and args['name'] != '' and args['name'] in user['name']:
        return True
    
    if 'age' in args and args['age'] != '':
        age = int(args['age'])
        ageRange = [age, age-1, age + 1]

        if user['age'] in ageRange:
            return True
        
    if 'occupation' in args and args['occupation'] and args['occupation'] in user['occupation']:
        return True
    
    return False

