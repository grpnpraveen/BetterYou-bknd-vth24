import os
import json

import ollama
from config import Config
from google_images_search import GoogleImagesSearch
from flask import Blueprint, request, json, Response

from utils.users import register_users, get_user


generate_api = Blueprint('model', __name__)


if not "llama3.1" in ollama.list().get("models"):                                     
    ollama.pull("llama3.1")                                                            




@generate_api.route("/api/generate_diet_plan/<username>", methods=["GET"])
def generate_diet_plan(username):
    '''
        To generate diet plan
    '''
    # return Response(json.dumps({"message": "Please provide user prompt"}),
    #                 mimetype="application/json",
    #                 status=200)
    user_details = get_user({"user_name": username})
    request_json = request.get_json()
    user_prompt = request_json.get("user_prompt")

    user_details_prefix_prompt = create_user_prefix_prompt(user_details)
    diet_plan = generate_recipe_recommendation(user_details_prefix_prompt, user_prompt)
    return Response(json.dumps(diet_plan),
                    mimetype="application/json",
                    status=200)

def create_user_prefix_prompt(data):
    user_details_prefix_prompt = "Type your message: Give help you with a healthy diet plan and exercises that are beneficial for your overall health, by the way if you need my details, here they are \n "
    for key, value in data["data"].items():
        if value is None:
            continue
        if key == "user_name" or key == "email" or key == "_id" or key == "response" or key == "mobile" or key == "address":
            continue
        if key == "preferred_food":
            user_details_prefix_prompt += f"My preferred food is {value}. add that atleat twice a week. "
        if key == "diet_plan":
            user_details_prefix_prompt += f"The user's diet plan is the following json: {value}. "
        user_details_prefix_prompt += f"{key} is {value}. "
    return user_details_prefix_prompt

def generate_recipe_recommendation(user_details_prefix_prompt, user_prompt=None):
    if user_prompt is None:
        user_prompt = ". Can you please provide some recommendations?"
    bot_input = user_details_prefix_prompt + user_prompt
    print("Bot input: ", bot_input)


    # Ensure bot_input is a list of dictionaries
    messages = [{"role": "user", "content": bot_input}]

    stream = ollama.chat(model="llama3.1", messages=messages, stream=True)
    bot_response = ""
    for chunk in stream:
        content = chunk["message"]["content"]
        print(content, end='', flush='')  
        bot_response += content
    print(bot_response)
    return bot_response
#     messages = []
#     message={"role":"user","content":"""Please help me with healthy diet plan \ 
#  gender is Male. age is 22. religion is hindu. sex is hetero. occupation is student. height is 6 feet. weight is 120 kg. medical_condition is None. mental_health is None. physical_activity_level is normal. habits is None. time_comitment is 30 mins. My preferred food is All. add that atleat twice a week. preferred_food is All. preferred_cusine is None. preferred_exercise is None. ideal_weight is 90 kgs. ideal_fitness_level is able to run marathon. . Can you please provide some recommendations?
# I'd be happy to help you with a healthy diet plan."""}   

#     messages.append(message)                                                            # Append message to the log
#     stream=ollama.chat(model="llama3.1",messages=messages,stream=True)                 # Call the Ollama server and return a stream
#     ai_response=[]                                                                      # This contains AI Response chunks
#     for chunk in stream:                                                                # Iterate through the stream
#         content=chunk["message"]["content"]                                             # Get the content from the server response
#         ai_response.append(content)                                                     # Append the content to the AI Response
#         print(content,end='',flush='')                                                  # Print each chunk in the stream
#     messages.append({"role":"assistant","content":"".join(ai_response)})  
#     return ai_response




# # you can provide API key and CX using arguments,
# # or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
# gis = GoogleImagesSearch(Config.GCP_API_KEY, Config.SEARCH_ENGINE_ID)


# _search_params = {
#     'q': 'Guacamole',
#     'num': 10,
#     'fileType': 'jpg',
#     'rights': 'cc_publicdomain',
#     'safe': 'active', ##
#     'imgType': 'photo', ##
#     'imgSize': 'large', ##
#     'imgDominantColor': 'imgDominantColorUndefined', ##
#     'imgColorType': 'color' ##
# }

# # this will only search for images:
# gis.search(search_params=_search_params)

# for image in gis.results():
#     if "wiki" in image.url:
#         print(image.url)
    