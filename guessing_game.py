# Simple guessing game

# define number to be guessed
guess_num = 5

# define variable to hold the user's guess
user_guess = None

# loop to continue to prompt the user until they guess correctly
while user_guess != guess_num:
    user_guess = int(input("What's your guess (between 1 and 10)? "))
    if user_guess < guess_num:
        print("Too low!")
    elif user_guess > guess_num:
        print("Too high!")
    else:
        print("Correct!")