# Cafe Menu - Flat Dictionary
cafe_menu = {
    "Coffee - Espresso": 80,
    "Coffee - Cappuccino": 120,
    "Coffee - Latte": 130,
    "Coffee - Americano": 100,
    "Coffee - Mocha": 140,
    "Tea - Masala Chai": 60,
    "Tea - Green Tea": 70,
    "Tea - Lemon Tea": 65,
    "Tea - Black Tea": 60,
    "Tea - Herbal Tea": 75,
    "Snacks - Veg Sandwich": 90,
    "Snacks - Grilled Cheese": 110,
    "Snacks - French Fries": 80,
    "Snacks - Maggie": 70,
    "Snacks - Garlic Bread": 85,
    "Desserts - Brownie": 100,
    "Desserts - Muffin": 90,
    "Desserts - Ice Cream": 80,
    "Desserts - Cheesecake": 150,
    "Desserts - Choco Lava Cake": 120,
    "Cold Beverages - Iced Coffee": 130,
    "Cold Beverages - Cold Drink": 50,
    "Cold Beverages - Milkshake": 120,
    "Cold Beverages - Smoothie": 140,
    "Cold Beverages - Iced Tea": 100
}

print("Welcome to YOUR CAFE!")
print("----- Café Menu -----\n")
for item, price in cafe_menu.items():
    print(f"{item}: ₹{price}")

order_total = 0

while True:
    item = input("\nEnter the name of the item you want to order (or type 'quit' to finish): ")
    if item.lower() == "quit":
        break
    if item in cafe_menu:
        order_total += cafe_menu[item]
        print(f"Item '{item}' has been added to your order.")
    else:
        print(f"Item '{item}' is not available! Please check the spelling or try another item.")

print(f"\nThe total amount of your order is ₹{order_total}.")
print("Thank you for ordering with YOUR CAFE! ")
