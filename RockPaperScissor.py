import random
print("WELCOME TO ROCK PAPER SCISSOR GAME")
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image=[rock,paper,scissor]
user_choice = int(input("what do you choose. Type 0 for Rock, 1 for Paper And 2 for Scissors\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("compter choose ")
print(game_image[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("You types an invalid numebr. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You wins!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You wins!")
elif computer_choice == user_choice:
    print("It's a Draw!")

