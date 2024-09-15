from db_wrappers.dbutils import insert_or_update_tasks, get_task_for, get_task_by_date, remove_task

def update_tasks(tasks, user_name):

    res = insert_or_update_tasks(user_name, tasks)

    if res:
        return res
    else:
        return "no action taken"

def get_user_tasks(user_name):
    res = get_task_for(user_name)
    if res:
        return res
    else:
        return []

def get_tasks_with_date(user_name,date):
    res = get_task_by_date(user_name,date)
    return res

def del_task(username,date,task_name,point):
    res = remove_task(username,date,task_name,point)
    return res

def calculate_health_score_fo(carbs, fat, protein, calories):
    # Define the ideal percentage ranges for each macronutrient
    ideal_carbs_percent = (45, 65)  # Ideal 45-65% of calories from carbs
    ideal_fat_percent = (20, 35)    # Ideal 20-35% of calories from fat
    ideal_protein_percent = (10, 35) # Ideal 10-35% of calories from protein
    
    # Calculate the actual percentage of calories from each macronutrient
    carbs_calories = carbs * 4
    fat_calories = fat * 9
    protein_calories = protein * 4

    total_macronutrient_calories = carbs_calories + fat_calories + protein_calories

    # Actual percentages of total calorie intake from each macronutrient
    carbs_percent = (carbs_calories / calories) * 100
    fat_percent = (fat_calories / calories) * 100
    protein_percent = (protein_calories / calories) * 100

    # Score calculation: Closer the percentage to the ideal range, higher the score
    def score_macronutrient(actual, ideal_range):
        if actual < ideal_range[0]:
            return (actual / ideal_range[0]) * 50  # Less than ideal, score out of 50
        elif actual > ideal_range[1]:
            return (ideal_range[1] / actual) * 50  # More than ideal, penalize by scaling
        else:
            return 50 + ((actual - ideal_range[0]) / (ideal_range[1] - ideal_range[0])) * 50  # Within range, score out of 100

    # Calculate the score for each macronutrient
    carbs_score = score_macronutrient(carbs_percent, ideal_carbs_percent)
    fat_score = score_macronutrient(fat_percent, ideal_fat_percent)
    protein_score = score_macronutrient(protein_percent, ideal_protein_percent)

    # Average score across all macronutrients
    overall_score = (carbs_score + fat_score + protein_score) / 3

    return int(round(round(overall_score, 0)/10,0))

def calculate_health_score_ex(calories_burned, duration):
    # Define the ideal range of calories burned based on activity level
    ideal_calories_burned = (400, 600)  # Target range for moderate activity
    intensity = 'medium'  # Can be 'low', 'medium', or 'high'
    # Intensity multiplier (optional) - we give more weight to higher intensity workouts
    intensity_multiplier = {
        'low': 0.8,   # 80% of the ideal
        'medium': 1.0, # 100% of the ideal
        'high': 1.2   # 120% of the ideal
    }

    # Apply intensity multiplier to calories burned
    adjusted_calories_burned = calories_burned * intensity_multiplier[intensity]
    
    # Score based on how close the calories burned are to the ideal range
    def score_calories_burned(actual, ideal_range):
        if actual < ideal_range[0]:
            return (actual / ideal_range[0]) * 50  # Less than ideal, score out of 50
        elif actual > ideal_range[1]:
            return (ideal_range[1] / actual) * 50  # More than ideal, scale down
        else:
            return 50 + ((actual - ideal_range[0]) / (ideal_range[1] - ideal_range[0])) * 50  # Within range, score out of 100
    
    calories_score = score_calories_burned(adjusted_calories_burned, ideal_calories_burned)
    
    # Add bonus points based on duration
    if duration >= 60:
        duration_score = 100  # Full score for 60+ minutes of exercise
    elif duration >= 30:
        duration_score = 75  # Partial score for 30-59 minutes
    else:
        duration_score = 50  # Minimum score for < 30 minutes

    # Average the scores with higher weight given to calories burned
    overall_score = (calories_score * 0.7) + (duration_score * 0.3)
    
    return round(round(overall_score,0)/10,0)

# # Example usage
# calories_burned = 500  # Calories burned during exercise

# duration = 45  # Exercise duration in minutes

# score = calculate_health_score_ex(calories_burned, duration)




# score = calculate_health_scoref(carbs, fat, protein, calories)


