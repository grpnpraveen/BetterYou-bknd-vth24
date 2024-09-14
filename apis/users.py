from flask import Blueprint,request,json,Response
from utils.users import register_users, get_user

users_api = Blueprint('users', __name__)



@users_api.route("/set/profile", methods=["POST"])  # set profile 
def setprofile():
    '''
        To set data about the user
    '''
    user_data = request.get_json()

    response_payload = register_users(user_data)
     
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)


@users_api.route("/get/profile/<username>", methods=["GET"])  # view profile 
def getprofile(username):
    '''
        To get data about the user
    '''
    
    if username:
        response_payload = get_user(username)
        return Response(json.dumps(response_payload),
                        mimetype="application/json",
                        status=200)
    else:
        response_payload = "Url param username is missing."
        return Response(json.dumps(response_payload),
                        mimetype="application/json",
                        status=404)

