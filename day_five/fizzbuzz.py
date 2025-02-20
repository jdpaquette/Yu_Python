fizzbuzz = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        fizzbuzz.append("FizzBuzz")
    elif num % 3 == 0:
        fizzbuzz.append("Fizz")
    elif num % 5 == 0:
        fizzbuzz.append("Buzz")
    else:
        fizzbuzz.append(num)
for i in fizzbuzz:
    print(i)
