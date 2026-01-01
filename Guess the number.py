from random import randint
from art1 import logo
EASY_TURNS = 10
HARD_TURNS = 5
turns = 0
def check_answer(user_guess , actual_answer,turns):
    if user_guess > actual_answer:
        print("You guessed too high")
        return turns -1
    elif  user_guess < actual_answer:
        print("You guessed too low")
        return turns -1
    else:
        print(f"You guessed correctly.Your answer is {actual_answer}")


def set_difficulty():
    choose_a_difficulty=input("Choose a difficulty.Type 'easy or 'hard':")
    if choose_a_difficulty == "easy":
         return EASY_TURNS
    else :
         return HARD_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Psst , the correct answer is {answer}")

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess , answer,turns)
        if turns == 0:
            print ("You've run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again.")

game()