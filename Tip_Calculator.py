
print("Welcome to the tip calculator!")
bill= float(input("What's your total bill: $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15: "))
people= int(input("how many people to split the bill: "))
percentage= (tip/100)
calculation= float((bill * percentage + bill) / people)
print(f"Each person should pay: ${calculation}")

