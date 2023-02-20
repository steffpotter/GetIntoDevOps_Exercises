import random


# function to get the user action
def get_user_action():
    user_action = input("Enter a choice (R for rock, P for paper, S for scissors): ")

    if user_action != "R" and user_action != "P" and user_action != "S":
        print("Oops! Please enter a valid choice! R, P or S...")
        return -1

    if user_action == "R":
        return 0
    elif user_action == "P":
        return 1
    else:
        return 2


# function to find out who won
def find_winner(user_action, computer_action):

    choices = ["Rock", "Paper", "Scissors"]

    print(f"\nYou chose {choices[user_action]}, computer chose {choices[computer_action]}.\n")

    if user_action == computer_action:
        print(f"Both players selected {choices[user_action]}. It's a tie!")
    elif user_action == 0:
        if computer_action == 2:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == 1:
        if computer_action == 0:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == 2:
        if computer_action == 1:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


play_again = True


# function to check if the user wants to play again
def set_play_again():
    play_again_check = input("Play again? (y/n):")

    if play_again_check.lower() == "n":
        return False


# main loop
while play_again:
    user_action = get_user_action()

    if user_action == -1:
        continue

    computer_action = random.randint(0, 2)

    find_winner(user_action, computer_action)

    play_again = set_play_again()
