import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    return choices

def check_win(player, computer):
    # The f statement is a new way to format strings in Python 3.6+. It's called an f-string.
    # Is better than %s or .format() because it's easier to read and write.
    print(f"You chose {player} and the computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You win!"
        else:
            return "You lose!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return "You lose!"
    else:
        return "Something went wrong."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
