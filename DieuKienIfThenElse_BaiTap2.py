# Prompt user to input
weight = input("Enter your weight (pounds): ")
height = input("Enter your height (inches): ")

# Convert user input into float values
weight = float(weight)
height = float (height)

# Convert weight into kilograms and height into meters
weight = weight * 0.45359237
height = height * 0.0254

# Calculate BMI
bmi = weight / (height * height)

# Print health status
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")