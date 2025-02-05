print("welcome to car ride! ")
height = int(input("enter your height: "))
bill = 0

if height >= 120:
    print("you can ride") 
    age = int(input("enter your age: "))
    if age <= 12:
        bill = 5
        print("child pay $5")
    elif age <=18:
        bill = 7
        print("youth pay $7")
    else:
        bill = 12
        print("adult pay $12")
    photo = input("do you want photo. Type Yes(y) or No(n). ")
    if photo == "y":
        bill += 3
        print(f"your total bill is {bill}")
    
else:
    print("you can't ride the car")