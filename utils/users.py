from db_wrappers.dbutils import add_user, find_record, get_user_profile
from utils.input_validator import validator
from exceptions import CustomErrors

global required_fields
required_fields = ["user_name", "email", "mobile", "gender", "age", "religion", "sex", "height", "weight", "medical_condition", "mental_health", "habits", "preferred_food", "ideal_weight", "ideal_fitness_level"]

def register_users(data):
    validations = {
                    "user_name": str,
                    "email":str,                    
                    "mobile":str,
                    "address":str,
                    "gender":str,
                    "age":int,
                    "religion":str,
                    "sex":str,
                    "occupation":str,
                    "height":int,
                    "weight":int,
                    "medical_condition":str,
                    "mental_health":str,
                    "physical_activity_level":str,
                    "habits":str,
                    "time_comitment":int,
                    "preferred_food":str,
                    "preferred_cusine":str,
                    "preferred_exercise":str,
                    "ideal_weight":int,
                    "ideal_fitness_level":int
                   }

    validation_messages = validator.validate_datatype(validations, data)

    print(validation_messages)

    if len(validation_messages):
            raise CustomErrors(validation_messages)
    for each_val in required_fields:
        if not validator.data_required(data[each_val]):
            raise CustomErrors(f"{each_val} is a required field.")
    
    email_error = validator.validate_email(email=data['email'])

    if email_error:
        raise CustomErrors(email_error)

    mobile_error = validator.validate_mobile(mobile=data['mobile'],
                                             length=10)
    if mobile_error:
        raise CustomErrors(mobile_error)
    

    if find_record({"user_name":  data["user_name"]}) != "new":
        response_payload = {"message": "username already existed, try another.",
                            "response": False,
                            }
        return response_payload

    else:
        payload =  add_user(data)
        response_payload = {
                            "message":"add user successfully",
                            "response":True,
                           }
        return response_payload

    

def get_user(query):
    response = get_user_profile(query)
    if response:
        response_payload = {
                            "data":response,
                            "response":True,
                           }
        return response_payload

    response_payload = {
                         "message":"User Not Found",
                         "response":False,
                           }
    return response_payload
    


