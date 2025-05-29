logo= """
   _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
                                                                                      
"""
print(logo+"\n\n")


from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#function to check users guess against actual answer
def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess<actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")


#funtion to set difficulty

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #Choosing a random number between 1 to 100

    print("Welcome to number guessing game")
    print("I'm thinking of a number between 1 to 100.")

    #answer from random module
    answer = randint(1,100)

    #setting difficulty
    turns = set_difficulty()


    guess = 0
    while guess != answer:
        
        print(f"You have {turns} attempts remaining to guess then number.")
        #user guess a number
        guess = int(input("Make a guess: "))    


        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You've run out of gusses, you lose.")
            return 
        elif guess != answer: 
            print("Guess again.")


game()