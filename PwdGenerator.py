
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PythonPassword Generator!")
enter_letter= int(input("How many letters would you like in your password?\n"))
enter_symbols= int(input("How many symbols would you like?\n"))
enter_numbers= int(input("How many numbers would you like?\n"))

#Easy password

"""password= ""

for char in range(0, enter_letter):
    password += random.choice(letters)

for symbol in range(0, enter_symbols):
    password += random.choice(symbols)

for num in range(0, enter_numbers):
    password += random.choice(numbers)

print(password)"""



#Hard password

password_list= []

for char in range(0, enter_letter):
    password_list.append(random.choice(letters))

for symbol in range(0, enter_symbols):
    password_list.append(random.choice(symbols))

for num in range(0, enter_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
