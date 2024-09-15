from flask import Blueprint,request,json,Response
from utils.users import register_users, get_user

users_api = Blueprint('users', __name__)



@users_api.route("/api/profile", methods=["POST"])  # set profile 
def setprofile():
    '''
        To set data about the user
    '''
    user_data = request.get_json()

    user_data["diet_plan"] = {
    "friday": {
        "breakfast": {
            "calories": "300",
            "dish_name": "Greek yogurt with berries and granola",
            "dish_url": "https://www.google.com/search?q=Greek+yogurt+with+berries+and+granola&tbm=isch",
            "macros": {
                "carbs": "50g",
                "fat": "10g",
                "protein": "20g"
            },
            "time": "7:00 AM"
        },
        "date": "2024-09-13",
        "dinner": {
            "calories": "450",
            "dish_name": "Baked chicken breast with roasted bell peppers and quinoa",
            "dish_url": "https://www.google.com/search?q=Baked+chicken+breast+with+roasted+bell+peppers+and+quinoa&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "6:00 PM"
        },
        "lunch": {
            "calories": "350",
            "dish_name": "Grilled chicken breast with mixed greens salad and whole wheat crackers",
            "dish_url": "https://www.google.com/search?q=Grilled+chicken+breast+with+mixed+greens+salad+and+whole+wheat+crackers&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "12:00 PM"
        },
        "snacks": {
            "calories": "150",
            "dish_name": "Carrot sticks with hummus and whole wheat crackers",
            "dish_url": "https://www.google.com/search?q=Carrot+sticks+with+hummus+and+whole+wheat+crackers&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "5g"
            },
            "time": "3:00 PM"
        }
    },
    "monday": {
        "breakfast": {
            "calories": "300",
            "dish_name": "Greek yogurt with berries and granola",
            "dish_url": "https://www.google.com/search?q=Greek+yogurt+with+berries+and+granola&tbm=isch",
            "macros": {
                "carbs": "50g",
                "fat": "10g",
                "protein": "20g"
            },
            "time": "7:00 AM"
        },
        "date": "2024-09-09",
        "dinner": {
            "calories": "500",
            "dish_name": "Baked salmon with roasted asparagus and quinoa",
            "dish_url": "https://www.google.com/search?q=Baked+salmon+with+roasted+asparagus+and+quinoa&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "15g",
                "protein": "40g"
            },
            "time": "6:00 PM"
        },
        "lunch": {
            "calories": "350",
            "dish_name": "Grilled chicken breast with mixed greens salad and whole wheat crackers",
            "dish_url": "https://www.google.com/search?q=Grilled+chicken+breast+with+mixed+greens+salad+and+whole+wheat+crackers&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "12:00 PM"
        },
        "snacks": {
            "calories": "150",
            "dish_name": "Apple slices with almond butter",
            "dish_url": "https://www.google.com/search?q=Apple+slices+with+almond+butter&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "5g"
            },
            "time": "3:00 PM"
        }
    },
    "saturday": {
        "breakfast": {
            "calories": "250",
            "dish_name": "Scrambled eggs with spinach and whole wheat toast",
            "dish_url": "https://www.google.com/search?q=Scrambled+eggs+with+spinach+and+whole+wheat+toast&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "20g"
            },
            "time": "8:00 AM"
        },
        "date": "2024-09-14",
        "dinner": {
            "calories": "500",
            "dish_name": "Baked salmon with roasted asparagus and quinoa",
            "dish_url": "https://www.google.com/search?q=Baked+salmon+with+roasted+asparagus+and+quinoa&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "15g",
                "protein": "40g"
            },
            "time": "7:00 PM"
        },
        "lunch": {
            "calories": "350",
            "dish_name": "Grilled chicken breast with mixed greens salad and whole wheat crackers",
            "dish_url": "https://www.google.com/search?q=Grilled+chicken+breast+with+mixed+greens+salad+and+whole+wheat+crackers&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "1:00 PM"
        },
        "snacks": {
            "calories": "150",
            "dish_name": "Rice cakes with almond butter and banana slices",
            "dish_url": "https://www.google.com/search?q=Rice+cakes+with+almond+butter+and+banana+slices&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "5g"
            },
            "time": "3:00 PM"
        }
    },
    "status": "success",
    "sunday": {
        "breakfast": {
            "calories": "300",
            "dish_name": "Greek yogurt with honey and almonds",
            "dish_url": "https://www.google.com/search?q=Greek+yogurt+with+honey+and+almonds&tbm=isch",
            "macros": {
                "carbs": "50g",
                "fat": "15g",
                "protein": "20g"
            },
            "time": "8:00 AM"
        },
        "date": "2024-09-15",
        "dinner": {
            "calories": "450",
            "dish_name": "Grilled chicken breast with roasted bell peppers and quinoa",
            "dish_url": "https://www.google.com/search?q=Grilled+chicken+breast+with+roasted+bell+peppers+and+quinoa&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "7:00 PM"
        },
        "lunch": {
            "calories": "400",
            "dish_name": "Turkey and cheese wrap with mixed greens",
            "dish_url": "https://www.google.com/search?q=Turkey+and+cheese+wrap+with+mixed+greens&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "15g",
                "protein": "30g"
            },
            "time": "1:00 PM"
        },
        "snacks": {
            "calories": "150",
            "dish_name": "Apple slices with peanut butter",
            "dish_url": "https://www.google.com/search?q=Apple+slices+with+peanut+butter&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "5g"
            },
            "time": "3:00 PM"
        }
    },
    "thursday": {
        "breakfast": {
            "calories": "250",
            "dish_name": "Scrambled eggs with mushrooms and whole wheat toast",
            "dish_url": "https://www.google.com/search?q=Scrambled+eggs+with+mushrooms+and+whole+wheat+toast&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "20g"
            },
            "time": "7:00 AM"
        },
        "date": "2024-09-12",
        "dinner": {
            "calories": "500",
            "dish_name": "Grilled salmon with roasted asparagus and quinoa",
            "dish_url": "https://www.google.com/search?q=Grilled+salmon+with+roasted+asparagus+and+quinoa&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "15g",
                "protein": "40g"
            },
            "time": "6:00 PM"
        },
        "lunch": {
            "calories": "400",
            "dish_name": "Turkey and cheese wrap with mixed greens",
            "dish_url": "https://www.google.com/search?q=Turkey+and+cheese+wrap+with+mixed+greens&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "15g",
                "protein": "30g"
            },
            "time": "12:00 PM"
        },
        "snacks": {
            "calories": "150",
            "dish_name": "Apple slices with peanut butter",
            "dish_url": "https://www.google.com/search?q=Apple+slices+with+peanut+butter&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "5g"
            },
            "time": "3:00 PM"
        }
    },
    "tuesday": {
        "breakfast": {
            "calories": "250",
            "dish_name": "Scrambled eggs with spinach and whole wheat toast",
            "dish_url": "https://www.google.com/search?q=Scrambled+eggs+with+spinach+and+whole+wheat+toast&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "20g"
            },
            "time": "7:00 AM"
        },
        "date": "2024-09-10",
        "dinner": {
            "calories": "450",
            "dish_name": "Grilled chicken breast with roasted bell peppers and quinoa",
            "dish_url": "https://www.google.com/search?q=Grilled+chicken+breast+with+roasted+bell+peppers+and+quinoa&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "6:00 PM"
        },
        "lunch": {
            "calories": "400",
            "dish_name": "Turkey and avocado wrap with mixed greens",
            "dish_url": "https://www.google.com/search?q=Turkey+and+avocado+wrap+with+mixed+greens&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "15g",
                "protein": "30g"
            },
            "time": "12:00 PM"
        },
        "snacks": {
            "calories": "150",
            "dish_name": "Carrot sticks with hummus and whole wheat crackers",
            "dish_url": "https://www.google.com/search?q=Carrot+sticks+with+hummus+and+whole+wheat+crackers&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "5g"
            },
            "time": "3:00 PM"
        }
    },
    "wednesday": {
        "breakfast": {
            "calories": "300",
            "dish_name": "Greek yogurt with honey and almonds",
            "dish_url": "https://www.google.com/search?q=Greek+yogurt+with+honey+and+almonds&tbm=isch",
            "macros": {
                "carbs": "50g",
                "fat": "15g",
                "protein": "20g"
            },
            "time": "7:00 AM"
        },
        "date": "2024-09-11",
        "dinner": {
            "calories": "400",
            "dish_name": "Baked chicken breast with roasted broccoli and quinoa",
            "dish_url": "https://www.google.com/search?q=Baked+chicken+breast+with+roasted+broccoli+and+quinoa&tbm=isch",
            "macros": {
                "carbs": "60g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "6:00 PM"
        },
        "lunch": {
            "calories": "350",
            "dish_name": "Grilled chicken breast with mixed greens salad and whole wheat crackers",
            "dish_url": "https://www.google.com/search?q=Grilled+chicken+breast+with+mixed+greens+salad+and+whole+wheat+crackers&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "40g"
            },
            "time": "12:00 PM"
        },
        "snacks": {
            "calories": "150",
            "dish_name": "Rice cakes with almond butter and banana slices",
            "dish_url": "https://www.google.com/search?q=Rice+cakes+with+almond+butter+and+banana+slices&tbm=isch",
            "macros": {
                "carbs": "30g",
                "fat": "10g",
                "protein": "5g"
            },
            "time": "3:00 PM"
        }
    }
}
    user_data["workout_plan"] = {
    "friday": {
        "calories_burned": "600",
        "date": "2024-09-13",
        "exercises": [
            {
                "name": "Rowing Machine",
                "reps": 20,
                "sets": 3
            },
            {
                "name": "Elliptical Trainer",
                "reps": 15,
                "sets": 2
            },
            {
                "name": "Cycling",
                "reps": 30,
                "sets": 1
            }
        ],
        "time": "60 minutes",
        "workout_name": "Cardio Day"
    },
    "monday": {
        "calories_burned": "400",
        "date": "2024-09-09",
        "exercises": [
            {
                "name": "Downward-Facing Dog",
                "reps": 30,
                "sets": 4
            },
            {
                "name": "Warrior Pose",
                "reps": 20,
                "sets": 3
            },
            {
                "name": "Tree Pose",
                "reps": 15,
                "sets": 2
            }
        ],
        "time": "60 minutes",
        "workout_name": "Yoga Day"
    },
    "saturday": {
        "calories_burned": "600",
        "date": "2024-09-14",
        "exercises": [
            {
                "name": "Treadmill Run",
                "reps": 20,
                "sets": 3
            },
            {
                "name": "Stationary Bike",
                "reps": 15,
                "sets": 3
            },
            {
                "name": "Swimming Laps",
                "reps": 10,
                "sets": 2
            }
        ],
        "time": "60 minutes",
        "workout_name": "Cardio Day"
    },
    "status": "success",
    "sunday": {
        "calories_burned": "900",
        "date": "2024-09-15",
        "exercises": [
            {
                "name": "Squats",
                "reps": 12,
                "sets": 4
            },
            {
                "name": "Deadlifts",
                "reps": 8,
                "sets": 3
            },
            {
                "name": "Bench Press",
                "reps": 10,
                "sets": 3
            }
        ],
        "time": "90 minutes",
        "workout_name": "Strength Training Day"
    },
    "thursday": {
        "calories_burned": "900",
        "date": "2024-09-12",
        "exercises": [
            {
                "name": "Lunges",
                "reps": 12,
                "sets": 4
            },
            {
                "name": "Push-ups",
                "reps": 15,
                "sets": 3
            },
            {
                "name": "Rows",
                "reps": 10,
                "sets": 2
            }
        ],
        "time": "90 minutes",
        "workout_name": "Strength Training Day"
    },
    "tuesday": {
        "calories_burned": "550",
        "date": "2024-09-10",
        "exercises": [
            {
                "name": "Burpees",
                "reps": 20,
                "sets": 3
            },
            {
                "name": "Jumping Rope",
                "reps": 15,
                "sets": 2
            },
            {
                "name": "Mountain Climbers",
                "reps": 30,
                "sets": 1
            }
        ],
        "time": "45 minutes",
        "workout_name": "High-Intensity Interval Training (HIIT) Day"
    },
    "wednesday": {
        "date": "2024-09-11",
        "workout_name": "Rest Day"
    }
}

    response_payload = register_users(user_data)
     
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)


@users_api.route("/api/profile/<username>", methods=["GET"])  # view profile 
def getprofile(username):
    '''
        To get data about the user
    '''
    if username:
        try:
            query = {"user_name": username}
            response_payload = get_user(query)
            return Response(json.dumps(response_payload),
                            mimetype="application/json",
                            status=200)
        except Exception as e:
            response_payload = {"message": str(e)}
            return Response(json.dumps(response_payload),
                            mimetype="application/json",
                            status=404)
    else:
        response_payload = "Url param username is missing."
        return Response(json.dumps(response_payload),
                        mimetype="application/json",
                        status=404)

