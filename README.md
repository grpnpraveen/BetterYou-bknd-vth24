# Better You, for Better Tomorrow - Project Backend [ Personalized Health and Fitness Web App BetterYou-bknd-vth24 ]

<img src="https://github.com/grpnpraveen/BetterYou-bknd-vth24/blob/main/logo.png" alt="BetterYou Logo" width="200"/>


BetterYou is a comprehensive web application focused on promoting healthy eating habits and physical fitness. By leveraging user data and advanced algorithms, BetterYou generates personalized diet and workout plans, while incorporating a rewarding point system to encourage healthy choices.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Diet and Workout Plan Generation](#diet-and-workout-plan-generation)
- [Reward System](#reward-system)
- [Analytics](#analytics)

- Presentatioon : https://www.canva.com/design/DAGQ0tg3s4Y/HNGLBUQOz-xB4Rt8Jq6Ndg/edit?utm_content=DAGQ0tg3s4Y&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton 
## Features

- Personalized diet plans based on user preferences and health goals
- Custom workout routines tailored to individual fitness levels
- Reward system to incentivize healthy choices
- Comprehensive user profiling for accurate recommendations
- Analytics dashboard for tracking progress and user diversity

## Technology Stack

<img src="https://github.com/grpnpraveen/BetterYou-bknd-vth24/blob/main/2.png" alt="BetterYou Tech stack" width="350"/>

- **Backend Framework**: Flask with Blueprint architecture
- **Database**: MongoDB Atlas
- **AI Model**: LLaMA 3.1 for personalized recommendations
- **Analytics**: MongoDB Charts for user analytics and diversity insights

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/betteryou.git
   cd betteryou
   ```

2. Install dependencies:

    Ensure you have Python 3.8+ installed. Create a virtual environment and install the required packages.
  
   ```bash
   python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

   ```

3. Set up MongoDB Atlas:

    Create a MongoDB Atlas account, set up a cluster, and add the .env file with your database credentials.

4. Access the app:
    Open your browser and navigate to https://betteryou.wiki

   
### Diet and Workout Plan Generation

For generating personalized diet and workout plans, BetterYou utilizes the **GAN Olama 3.1** model. This advanced Generative Adversarial Network (GAN) is designed to create optimized and tailored plans based on individual user data.

### How It Works

1. **Data Input:** The model takes detailed user information, including medical history, physical activity levels, and personal goals.

2. **Diet Plan Generation:** GAN Olama 3.1 processes this information to create a customized diet plan that meets the user's nutritional needs and preferences. The generated plan considers macronutrient ratios and personal food preferences.

3. **Workout Plan Generation:** Similarly, the model generates a workout plan tailored to the user’s fitness level and goals. This plan includes exercises designed to maximize calorie burn and improve overall fitness.

### Features

- **Personalization:** The use of GAN Olama 3.1 ensures that the plans are highly personalized, addressing individual health conditions, fitness levels, and dietary needs.

- **Optimization:** The model optimizes diet and workout plans to achieve the best results based on the user’s inputs.

- **Adaptability:** Plans can be adjusted and refined over time based on user feedback and progress.

GAN Olama 3.1 helps BetterYou deliver precise and effective diet and workout plans, enhancing the overall user experience and supporting better health outcomes.



### Reward System

  # Calculation

- **Diet Rewards:** Calculated based on adherence to ideal macronutrient percentages:
  - Carbs: 45-65% of total calories
  - Fat: 20-35% of total calories
  - Protein: 10-35% of total calories
  
- **Workout Rewards:** Based on calories burned during workouts.

## Analytics

BetterYou utilizes MongoDB Atlas Charts to gain insights into user data, track diversity, and monitor various metrics. The analytics section provides valuable information to enhance user experience and improve the effectiveness of diet and workout plans.

### Features

- **User Diversity Analysis:** MongoDB Atlas Charts helps visualize demographic and health-related diversity among users. This includes age distribution, gender ratios, and geographic locations, allowing BetterYou to tailor services to different user groups.

- **Health and Fitness Metrics:** Charts display various health and fitness metrics such as average weight, height, physical activity levels, and adherence to diet plans. This helps in understanding trends and making data-driven decisions for personalized recommendations.

- **Diet Adherence Tracking:** Analyze user compliance with recommended macronutrient distributions. Charts can show how well users adhere to the ideal percentages for carbs, fat, and protein, and how this correlates with their reward points and overall progress.

- **Workout Performance:** Monitor workout performance metrics, including calories burned and exercise frequency. This data helps in evaluating the effectiveness of workout plans and making adjustments based on user feedback and performance.

- **Progress Over Time:** Track user progress over time by visualizing changes in fitness levels, weight, and other relevant metrics. This allows users and administrators to see long-term trends and the impact of interventions.


   
