def bmiCalculator(weight: float, height: float, age: int):
    height: float = height*100
    bmi: float = weight / (height ** 2)
    
    categoryDataset = {
        "UDW": ["Underweight", "underweight"],
        "MUD": ["Mildly Underweight", "mildly underweight"],
        "UDW": ["Severely Underweight", "severely underweight"],
        "NRM": ["Normal weight", "normal weight"],
        "OVW": ["Overweight", "overweight"],
        "OB1": ["Obesity class I", "obesity class I"],
        "OB2": ["Obesity class II", "obesity class II"],
        "OB3": ["Obesity class III", "obesity class III"]
    }

    # Determine the category based on age
    if age < 18:  # For children and teens
        if bmi < 16:
            cat = 'UDW'  # Severely Underweight
        elif 16 <= bmi < 17:
            cat = 'MUD'  # Mildly Underweight
        elif 17 <= bmi < 18.5:
            cat = 'UDW'  # Underweight
        elif 18.5 <= bmi < 24.9:
            cat = 'NRM'  # Normal weight
        elif 25 <= bmi < 29.9:
            cat = 'OVW'  # Overweight
        elif 30 <= bmi < 34.9:
            cat = 'OB1'  # Obesity class I
        elif 35 <= bmi < 39.9:
            cat = 'OB2'  # Obesity class II
        else:
            cat = 'OB3'  # Obesity class III
    else:  # For adults
        if bmi < 18.5:
            cat = 'UDW'  # Underweight
        elif 18.5 <= bmi < 24.9:
            cat = 'NRM'  # Normal weight
        elif 25 <= bmi < 29.9:
            cat = 'OVW'  # Overweight
        elif 30 <= bmi < 34.9:
            cat = 'OB1'  # Obesity class I
        elif 35 <= bmi < 39.9:
            cat = 'OB2'  # Obesity class II
        else:
            cat = 'OB3'  # Obesity class III
    
    return cat, categoryDataset[cat]