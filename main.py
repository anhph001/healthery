from modules.bmiCalculator import bmiCalculator
from modules.dailyCalories import dailyCalories
from modules.dailyWaterIntake import dailyWaterIntake

age = 14 
weight = 58 # kg
height = 172 # cm
gender = "male"
activityLevel = "moderately_active"

print(f"{bmiCalculator(58, 1.72, 14)}")
print(dailyCalories(58, 172, 14, "male", activityLevel))
print(dailyWaterIntake(58, 14))