import random

"""
This is a simple number guessing game where the player 
has to guess a randomly generated number between 1 and 100.
The player can choose a difficulty level that determines 
the number of attempts they have to guess the number. 
The game provides feedback on whether the player's guess 
is too high or too low, and continues until the player either 
guesses the correct number or runs out of attempts.
After each game, the player is given the option to play again.
"""
def play_game():
    actual_guess = random.randint(1, 100)
    EASY_LEVEL = 10
    HARD_LEVEL = 5
    print("Welcome to the number guessing game")
    print("I'm thinking about a number between 1 and 100.")
# This function checks the player's guess against the actual number and provides feedback.
    def check_answer(guess, actual_guess):
        if guess == actual_guess:
            print("Congratulations! You guessed the correct number.")
        elif guess < actual_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# This function sets the difficulty level of the game based on the player's input.
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if level == "easy":
            return EASY_LEVEL
        elif level == "hard":
            return HARD_LEVEL
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")
            return set_difficulty()
# The main game loop where the player makes guesses until they either guess correctly or run out of attempts.
    guess = 0
    lives = set_difficulty()
    while guess != actual_guess and lives > 0:
        
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a number!")
            continue

        check_answer(guess, actual_guess)
        if guess != actual_guess:
            lives -= 1
        if guess != actual_guess and lives == 0:
            print("You've run out of guesses, you lose.")
            break
        if guess != actual_guess:
            print("Guess again.")
            print(f"You have {lives} attempts remaining to guess the number.")
play_game()

#The following loop allows the player to play the game multiple times based on their input.
while True:
    go_again = input("Do you want to play again? Type 'y' or 'n': ").lower().strip()
    if go_again == "y":
        print("\n"*100)
        play_game()
    elif go_again == "n":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Please type 'y' or 'n'.")
    
    