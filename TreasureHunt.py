

print("Welcome to Treasue island\nYour mission is to find the Treasure")
choice1=input('You are at crossroads, Where do you want to go? Type "left" and "right": ').lower()
if choice1 == "left":
    choice2 = input('You\'ve came to a lake, there is an island in the middle of the lake.'
                    ' Type "wait" to wait for a boat. '
                    'Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input('You arrived at the island unharmed. '
              'There is a House with 3 doors. one red, one yellow, one blue. '
              'Which color do you choose. ').lower()
        if choice3 == "red":
            print("it's room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("Congratulation! You found the Treasure. You Win")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over!")
        else: 
            print("Your choose a door which don't exists. Game Over!")
    else:
        print("You got attacked by shark. Game Over!") 
else:
    print("You Fell into a hole. Game Over!")
