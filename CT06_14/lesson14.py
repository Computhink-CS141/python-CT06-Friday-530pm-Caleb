print("Hello from lesson 14")

# Recap 1

# toppings = ["Mushrooms","Pepperoni","Pineapples","Onions","Sausage","Bacon","Extra cheese","Black olives","Green peppers","Fresh garlic",]
# for counter in range(len(toppings)):
#     print(counter+1, ":" , toppings[counter])

# selection = []
# question = "Please choose your pizza toppings by number: "
# ans = input(question)
# while not ans == "end":
#     index= int(ans)
#     selection.append(toppings[index-1])
#     ans = input(question)

# print("You have selected")
# for count in selection:
#     print(count)

# Task 1

# fruits= ["apple", "banana", "orange"]
# price = ["$12", "$23","$99"]

# for index in range (len(fruits)):
#     print(f"{fruits[index]} costs {price[index]} ")

# Task 2

# items = ["Apple", "Milk", "Bread", "Egg", "Chocolate"]
# stock = [15, 0, 8, 25, 3]
# for count in range(len(stock)):
    # qty = stock[count]
    # if qty == 0:
        # print(f"{items[count]} : Out of stock")
    # elif qty <10:
        # print(f"{items[count]} : Low Stock")
    # elif qty >=10:
        # print(f"{items[count]} : Well Stock")

# Task 2b

# ans=input("Buy something:")
# if ans in items:
    # found_index = items.index(ans)
    # qty = stock[found_index]
    # print(f"We have {qty} remaining")
# else:
    # print("Item not found in database.")

# Task3

shopping_list = ["Pens", "Pencils", "Erasers", "Notebooks"]
print(shopping_list)
num = int(input(" How many more stuff do you want to buy?"))

for count in range(num):
    ans= input("Whatdo you want to buy?")
    shopping_list.append (ans)
print(shopping_list)

