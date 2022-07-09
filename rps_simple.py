import random

# import random
# computer chooses rps randomly
# user inputs rps
# check win

def play():
    user_choice = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer_choice = random.choice(['r', 'p', 's'])

    print(is_win(user_choice, computer_choice))


def is_win(user, computer):
    if user == computer:
        return f"Computer choose {computer}. It is a tie"
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return f"Computer choose {computer}. Congratulations, you won!"
    else:
        return f"Computer choose {computer}. Sorry, you lost"


play()