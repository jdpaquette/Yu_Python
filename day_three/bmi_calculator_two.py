height = int(input("Enter you height in inches: "))
weight = float(input("Enter you weight in pounds: "))
bmi = round((weight / (height**2)) * 703, 2)
print("Your BMI is: ", bmi)
if bmi >= 25:
    print("You are overweight!")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight!")
else:
    print("You are underweight!")
