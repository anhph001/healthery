def dailyCalories(weight: float, height: float, age: int, gender: str, activitylevel: str):
    # Calculate Basal Metabolic Rate (BMR) using Mifflin-St Jeor equation
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Activity level multipliers
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725,
        "super_active": 1.9
    }
    
    multiplier = activity_multipliers.get(activitylevel.lower(), 1.2)
    
    calories = bmr * multiplier

    if age < 18:
        calories *= 1.2  # Additional multiplier for children/teens
    elif age >= 18:
        if gender.lower() == 'male':
            calories *= 1.1  # Slightly higher for adult males
        else:
            calories *= 1.05  # Slightly higher for adult females

    return calories