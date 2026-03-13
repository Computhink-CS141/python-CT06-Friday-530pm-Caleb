print("Hello from lesson 8")

# product = 1
# for count in range(1,6):
#     question = input("What is number #" + str(count) + "?")
#     question = int(question)
#     product = product * question
# print("The final number is " + str(product))

# import time
# for count in range(1,11):
#     print("Zzzzzz")
# time.sleep(5)
# print("I am awake!!!!")

# Task 1

# time1 = input("How long do you want the timer to be?")
# time2 = time1
# time1 = int(time1) + 1 
# for count in range(1,time1):
#     time.sleep(1)
#     num = int(time2) - int(count)
#     print(str(num))

# Task 2a

# import random

# number = random.ranint (1,6)
# print("Your random number is " + str(number))

# Task 2b
# for count in range(1,21):
#     number = random.randint (0,9999)
#     print(number)

# Task 3

# isRainy = False
# isSunny = False
# isSchoolHoliday = True
# print(isRainy)

# print(55 == 55)
# print(isSunny == isSchoolHoliday)

# Task 4

# import random

# random_num = random.randint (1,10)

# num = input ("Guess a number:")
# if (num == str(random_num)):
#     print("Correct")
# else:
#     print("Wrong")

# print("The number is " + str(random_num))


# Task 7

ans = int(input("Choose a number:"))
remd = ans % 2

if remd == 0 :
    print("True")
else:
    print("False")
