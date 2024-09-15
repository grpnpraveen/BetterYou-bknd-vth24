from flask import Blueprint,request,json,Response
from utils.tasks import calculate_health_score_fo,calculate_health_score_ex, update_tasks, get_user_tasks, get_tasks_with_date, del_task
from utils.users import get_user
tasks_api = Blueprint('tasks', __name__)

days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

type_of_meal = ["snacks","lunch", "dinner", "breakfast"]

@tasks_api.route("/api/tasks/create/", methods=["GET"])  
# def create_tasks():
def create_tasks(week_data,is_food,user_name):

    # user_name = "t1"
    # query = {"user_name": user_name}
    # response_payload = get_user(query)

    # week_data = dict(response_payload["data"]["diet_plan"])
    # is_food = True

    # week_data = dict(response_payload["data"]["workout_plan"])
    # is_food = False
    tasks = {}
    cloud_tasks = dict(get_user_tasks(user_name)).get("tasks",[])
    print(cloud_tasks)
    if is_food:
        # cat = "fo"
         
        for day in days_of_week:
            
            if day in week_data:
                # each_task["cat"] = cat
                current_day = week_data[day]
                if len(cloud_tasks)==0:
                    tasks[current_day["date"]] = []
                else:
                    tasks[current_day["date"]] = cloud_tasks[current_day["date"]]
                for meal in type_of_meal:
                    if meal in current_day:
                        macros = current_day[meal]["macros"]
                        # carbs, fat, protein = int(macros["carbs"]), int(macros["fat"]), int(macros["protein"])

                        points = calculate_health_score_fo(40,15,10,int(current_day[meal]["calories"]))
                        # points = calculate_health_score_fo(carbs, fat, protein,int(current_day[meal]["calories"]))
                        each_task = {}
                        each_task["points"] = points
                        each_task["Description"] = "Eat to complete the task"
                        each_task["task_name"] =  current_day[meal]["dish_name"]
                        tasks[current_day["date"]].append(each_task)

    else:
        # cat = "ex"
        for day in days_of_week:
            
            if day in week_data:
                current_day = week_data[day]
                if len(cloud_tasks)==0:
                    tasks[current_day["date"]] = []
                else:
                    tasks[current_day["date"]] = cloud_tasks[current_day["date"]]
                if "calories_burned" in current_day:
                    time = 60
                    if "time" in current_day:
                        time = int(current_day["time"][0:2])

                    points = calculate_health_score_ex(int(current_day["calories_burned"].split("-")[0]), time)
                    each_task = {}
                    each_task["points"] = points
                    each_task["Description"] = "Do exercise to complete the task"
                    each_task["task_name"] =  current_day["workout_name"]
        
                    tasks[current_day["date"]].append(each_task)
    # Tasks has the data now 

    res = update_tasks(tasks,user_name)

    # response_payload = register_users(user_data)
    response_payload =  {
                            "message":res,
                            "response":True,
                           }
     
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)



@tasks_api.route("/api/tasks/complete/<username>/<date>/<task_name>/<point>", methods=["GET"])  
def complete_task(username,date,task_name,point):

    response_payload = del_task(username,date,task_name,point)
     
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)


@tasks_api.route("/api/tasks/<username>/<date>", methods=["GET"])  
def get_todays_tasks(username,date):

    res = get_tasks_with_date(username,date)
    
    if res:
        response_payload = res
    else:
        response_payload = "not found"
     
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)
