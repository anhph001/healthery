def dailyWaterIntake(weight: float, age: int) -> float:
    waterIntake = weight * 30

    if age < 18:
        waterIntake *= 1.1  # Slightly higher for children/teens
    elif age >= 65:
        waterIntake *= 0.9  # Slightly lower for seniors

    return waterIntake