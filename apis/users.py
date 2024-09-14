from flask import Blueprint,request,json,Response
from db_wrappers.connect_cluster import ConnectCluster
users_api = Blueprint('users', __name__)



@users_api.route("/get/profile", methods=["GET"])  # view profile 
def getprofile():
    '''
        To get data about the patient or the doctor
    '''
    cluster = ConnectCluster()
    collection = cluster.get_collection("betteryou", "users")
    data = collection.list_documents()
    response_payload = {
                        "message": "Data found",
                        "data": data,
                        "response": True
                        }
                        
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)