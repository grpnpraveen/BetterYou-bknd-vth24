import os
import json

import ollama
from config import Config
from google_images_search import GoogleImagesSearch
from flask import Blueprint, request, json, Response
from db_wrappers.dbutils import update_user_record, get_user_profile
from datetime import datetime, timedelta
# import traceback

from utils.users import register_users, get_user
from apis.tasks import create_tasks

generate_api = Blueprint('model', __name__)


if not "llama3.1" in ollama.list().get("models"):                                     
    ollama.pull("llama3.1")                                                            


gis = GoogleImagesSearch(Config.GCP_API_KEY, Config.SEARCH_ENGINE_ID)


def format_dates(data):
    today = datetime.today()
    today_day_number = today.weekday()  # Monday = 0, Sunday = 6

    def get_date_for_day(day_number):
        return (today + timedelta(days=(day_number - today_day_number))).strftime('%Y-%m-%d')
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    for i, day in enumerate(days_of_week):
        data[day]["date"] = get_date_for_day(i)

    return data

@generate_api.route("/api/generate_diet_plan/<username>", methods=["POST"])
def generate_diet_plan(username):
    '''
        To generate diet plan
    '''

    user_details = get_user({"user_name": username})
    request_json = request.get_json()
    print(request_json)
    user_prompt = request_json.get("user_prompt")

    user_details_prefix_prompt = create_user_prefix_prompt(user_details, "diet_plan")
    diet_plan = generate_recipe_recommendation(user_details_prefix_prompt, user_prompt)
    print(diet_plan)
    if diet_plan.get("status") != "error":
        update_user_record({"user_name": username}, {"diet_plan": diet_plan, "type": "diet_plan"})
        create_tasks(diet_plan,True,username)
    else:
        diet_plan = get_user_profile({"user_name": username}).get("diet_plan")
        create_tasks(diet_plan,True,username)
    return Response(json.dumps(diet_plan),
                    mimetype="application/json",
                    status=200)

def create_user_prefix_prompt(data, key):
    if key == "diet_plan":
        user_details_prefix_prompt = "Give a healthy diet plan that are beneficial for your overall health, by the way if you need my details, here they are \n "
    if key == "workout_plan":
        user_details_prefix_prompt = "Give a workout plan that are beneficial for your overall health, by the way if you need my details, here they are \n "
    for key, value in data["data"].items():
        if value is None:
            continue
        if key == "user_name" or key == "email" or key == "_id" or key == "response" or key == "mobile" or key == "address":
            continue
        if key == "preferred_food":
            user_details_prefix_prompt += f"My preferred food is {value}. add that atleat twice a week. "
        if key == "diet_plan":
            user_details_prefix_prompt += f"The user's diet plan for yesterday is the following json: {value}. "
        user_details_prefix_prompt += f"{key} is {value}. "
    return user_details_prefix_prompt

def generate_recipe_recommendation(user_details_prefix_prompt, user_prompt=None):
    if user_prompt is None:
        user_prompt = ". Can you please provide some diet and food recommendations for 1 week? Strictly, the output should be a JSON nothing else. do not add comments. example json format : ```json{'saturday':{'breakfast':{'time':'','dish_name':'','calories':'','macros':{'carbs':'','fat':'','protein':{}}},'lunch':{'time':'','dish_name':'','calories':'','macros':''}, 'dinner':{'time':'','dish_name':'','calories':'','macros':''},'snacks':{'time':'','dish_name':'','calories':'','macros':''}}}``` The output should just contain the JSON nothing else no javascript or Explainations."
    bot_input = user_details_prefix_prompt + user_prompt


    # Ensure bot_input is a list of dictionaries
    messages = [{"role": "user", "content": bot_input}]

    stream = ollama.chat(model="llama3.1", messages=messages, stream=True)
    bot_response = ""
    for chunk in stream:
        content = chunk["message"]["content"]
        # print(content, end='', flush='')  
        bot_response += content
    # print(bot_response)
    # return bot_response
    try:
        if "```json" in bot_response:
            bot_response = bot_response.split("```json")[1]
            bot_response = bot_response.split("```")[0]
        if "```" in bot_response:
            bot_response = bot_response.split("```")[1]
        # print(bot_response)
        bot_response = json.loads(bot_response)
        # print(bot_response)
        for key in bot_response:
            for key2 in bot_response[key]:
                try:
                    bot_response[key][key2]['dish_url'] = "https://www.google.com/search?q=" + bot_response[key][key2]['dish_name'].replace(" ", "+") + "&tbm=isch"
                except Exception as e:
                    pass
        bot_response = format_dates(bot_response)
        bot_response["status"] = "success"
        return bot_response
    except Exception as e:
        # traceback.print_exc()
        return {"error": f"Error in generating diet plan {e}", "status": "error"}


@generate_api.route("/api/generate_workout_recommendation/<username>", methods=["POST"])
def generate_workout_recommendation(username):
    '''
        To generate workout recommendation
    '''

    user_details = get_user({"user_name": username})
    print(user_details)
    if user_details:
        user_details_prefix_prompt = create_user_prefix_prompt(user_details, "workout_plan")
        workout_recommendation = generate_workout_recommendation(user_details_prefix_prompt)
        if workout_recommendation.get("status") != "error":
            update_user_record({"user_name": username}, {"workout_plan": workout_recommendation, "type": "workout_plan"})
            create_tasks(workout_recommendation,False,username)
        else:
            workout_recommendation = get_user_profile({"user_name": username})
            workout_recommendation = workout_recommendation.get("workout_plan")
            create_tasks(workout_recommendation,False,username)

        return Response(json.dumps(workout_recommendation),
                        mimetype="application/json",
                        status=200)
    else:
        return Response(json.dumps({"error": "User not found"}),
                        mimetype="application/json",
                        status=404)

def generate_workout_recommendation(user_details_prefix_prompt, user_prompt=None):
    if user_prompt is None:
        user_prompt = ". Can you please provide a workout plan for 1 week? Strictly, the output should be a JSON nothing else. do not add comments. example json format : ```json{'saturday':{'workout_name':'','exercises': [],'time':'','calories_burned':''}}``` The output should just contain the JSON nothing else no javascript or Explainations."
    bot_input = user_details_prefix_prompt + user_prompt

    # Ensure bot_input is a list of dictionaries
    messages = [{"role": "user", "content": bot_input}]

    stream = ollama.chat(model="llama3.1", messages=messages, stream=True)
    bot_response = ""
    for chunk in stream:
        content = chunk["message"]["content"]
        # print(content, end='', flush='')  
        bot_response += content
    # print(bot_response)
    # return bot_response
    try:
        if "```json" in bot_response:
            bot_response = bot_response.split("```json")[1]
            bot_response = bot_response.split("```")[0]
        if "```" in bot_response:
            bot_response = bot_response.split("```")[1]
        # print(bot_response)
        if "I can't" in bot_response:
            return {"error": "Please try again later"}
        bot_response = json.loads(bot_response.replace("miles", ""))
        # print(bot_response)
        bot_response = format_dates(bot_response)
        bot_response["status"] = "success"
        return bot_response
    except Exception as e:
        # traceback.print_exc()
        return {"error": f"Error in generating workout plan {e}", "status": "error"}
        
