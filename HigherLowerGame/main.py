import random 
from game_data import data

gamelogo = """
  _   _ _       _                 _                        
 | | | (_) __ _| |__   ___ _ __  | | _____      _____ _ __ 
 | |_| | |/ _` | '_ \ / _ \ '__| | |/ _ \ \ /\ / / _ \ '__|
 |  _  | | (_| | | | |  __/ |    | | (_) \ V  V /  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|    |_|\___/ \_/\_/ \___|_|   
          |___/                                            
"""
print(gamelogo)

score = 0


def format_data(account):
    #Format the account data into printable format
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, a {desc}, from {country}"


def check_answer(user_guess, a_followers, b_followers):
    #Take a user's guess and the follower counts and returns if they got it right.
    if a_followers > b_followers:
        return user_guess == 'a'
    else: 
        return user_guess == 'b'

game_should_continue = True

account_b = random.choice(data)

#Make game repetable
while game_should_continue:
    #Generate a random account from data
    

    #Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)



    print(f"Compare A : {format_data(account_a)}")

    vs = """
 __     ______   
 \ \   / / ___|  
  \ \ / /\___ \  
   \ V /  ___) | 
    \_/  |____/  
                 
               
    """

    print(vs)

    print(f"Against B : {format_data(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Clear screen
    print("\n" * 20)
    print(gamelogo)


    #Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    #Use if statement to check if user is correct

    #Give user feedback
    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

