print("Hello from lesson 10")

# Recap 1

import random

rannum = random.randint(1,15)

usernum = int(input("Choose a number between 1 to 15: "))
if usernum == rannum:
    print("Congratulations!")

# # Task 1

usernum = int(input("Choose a number:"))
if usernum > 0:
    print(str(usernum)+ " is positive")
elif int(usernum) < 0 :
    print(str(usernum)+ " is negative")
else:
    print("0 is not negative or positive.")

# Task 2

age = int(input("What is your age?"))
if age < 13:
    print("Child")
else:
    if age < 20:
        print("Teen")
    else:
        print("Adult")

# Task 3

temp = int(input("What is the temperature?"))
if temp >30:
    print("Go swim.")
elif 24 < temp < 30:
    print("Play basketball.")
elif 19< temp < 24:
    print("Go cycle.")
else:
    print("READ.")

# Task 4

score = int(input("What is the mark?"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
