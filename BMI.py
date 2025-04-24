def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculates Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The BMI value.

    Raises:
        ValueError: If weight_kg or height_m are not positive.
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Invalid input: Weight and height must be positive numbers.")
    
    return weight_kg / (height_m ** 2)


def interpret_bmi(bmi: float) -> str:
    """
    Interprets the BMI value and returns a category.

    Args:
        bmi (float): The BMI value.

    Returns:
        str: A string representing the BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        bmi_value = calculate_bmi(weight, height)
        bmi_category = interpret_bmi(bmi_value)
        
        print(f"Your BMI is {bmi_value:.2f}, which is considered '{bmi_category}'.")
    except ValueError as e:
        print(e)
