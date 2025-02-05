print("Welcome to Pizza Shop!")

size = input("What size pizza you want? S, M or L ")
pepperoni = input("Do you want to add Pepperoni in your pizza? Y or N: ")
extra_cheese = input("Do you want Extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You Typed the Wrong input.")
    exit()  

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
