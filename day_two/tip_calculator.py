# Build a tip calculator app
# Key points: total bill, tip percentage, number of people
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill?"))
total_bill = total * (1 + (percentage / 100))
split = total_bill / people
print(f"Total bill with tip: ${round(total_bill, 2)}")
print(f"Each person should pay: ${round(split, 2)}")
