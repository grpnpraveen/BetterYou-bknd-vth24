from flask import Blueprint,request,json,Response

users_api = Blueprint('users', __name__)



@users_api.route("/get/profile", methods=["GET"])  # view profile 
def getprofile():
    '''
        To get data about the patient or the doctor
    '''
    response_payload = {
                        "message": "Data found",
                                   
                        "response": True
                        }
                        
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)