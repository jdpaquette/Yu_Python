height = int(input("Enter you height in inches: "))
weight = int(input("Enter you weight in pounds: "))
bmi = round((weight / (height**2)) * 703, 2)
print("Your BMI is: ", bmi)
