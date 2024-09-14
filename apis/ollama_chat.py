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


gis = GoogleImagesSearch(Config.GCP_API_KEY, Config.SEARCH_ENGINE_ID)


@generate_api.route("/api/generate_diet_plan/<username>", methods=["GET"])
def generate_diet_plan(username):
    '''
        To generate diet plan
    '''

    user_details = get_user({"user_name": username})
    request_json = request.get_json()
    user_prompt = request_json.get("user_prompt")

    user_details_prefix_prompt = create_user_prefix_prompt(user_details)
    diet_plan = generate_recipe_recommendation(user_details_prefix_prompt, user_prompt)
    return Response(json.dumps(diet_plan),
                    mimetype="application/json",
                    status=200)

def create_user_prefix_prompt(data):
    user_details_prefix_prompt = "You are Meta AI, a friendly AI Assistant. Today's date is {Saturday, September 14, 2024}. Respond to the input as a friendly AI assistant, generating human-like text, and follow the instructions in the input if applicable. Keep the response concise and engaging, using Markdown when appropriate. The user live in {Country}, so be aware of the local context and preferences. Use a conversational tone and provide helpful and informative responses, utilizing external knowledge when necessary. Give help you with a healthy diet plan and exercises that are beneficial for your overall health, by the way if you need my details, here they are \n "
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
        user_prompt = ". Can you please provide some diet and food recommendations? Put the schedule in a json format for all days in the week. No other keys in the json instead of days of the week. Make sure there are not json decode error. Fill it with dishes closer to my preference. Don't leave it half empty and add comments like continue for the rest of the week/ similar to the otherday. Strictly, do not add comments. example: {\'monday':{\'breakfast':{\'time':'', 'dish_name':etc...'}\}\}."
    bot_input = user_details_prefix_prompt + user_prompt


    # Ensure bot_input is a list of dictionaries
    messages = [{"role": "user", "content": bot_input}]

    stream = ollama.chat(model="llama3.1", messages=messages, stream=True)
    bot_response = ""
    for chunk in stream:
        content = chunk["message"]["content"]
        # print(content, end='', flush='')  
        bot_response += content
    print(bot_response)
    # return bot_response
    try:
        bot_response = bot_response.split("```json")[1]
        bot_response = bot_response.split("```")[0]
        print(bot_response)
        bot_response = json.loads(bot_response)
        print(bot_response)
        for key in bot_response:
            for key2 in bot_response[key]:
                bot_response[key][key2]['dish_url'] = "https://www.google.com/search?q=" + bot_response[key][key2]['dish_name']
        return bot_response
    except Exception as e:
        return {"error": f"Error in generating diet plan {e}"}
    #             _search_params = {
    #                 'q': '',
    #                 'num': 1,
    #                 'fileType': 'jpg',
    #                 'rights': 'cc_publicdomain',
    #                 'safe': 'active', ##
    #                 'imgType': 'photo', ##
    #                 'imgSize': 'large', ##
    #                 'imgDominantColor': 'imgDominantColorUndefined', ##
    #                 'imgColorType': 'color' ##
    #             }
    #             _search_params['q'] = bot_response[key][key2]['dish_name']
    #             gis.search(search_params=_search_params)
    #             for image in gis.results():
    #                 if "wiki" in image.url:
    #                     bot_response[key][key2]['image_url'] = image.url
    #                     break
            
    #     return bot_response
    # except Exception as e:
    #     return {"error": "Error in generating diet plan"}
       
        
