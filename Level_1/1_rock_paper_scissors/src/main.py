import random
from utils import print_error, print_grey, print_success, print_warning, print_success_plain


class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    # player's choice
    def get_player_choice(self):
        print('---------------------')
        user_choice = input(f"Enter your choice ({' | '.join(self.choices)}):\n")
        user_choice = user_choice.lower()
        if user_choice in self.choices:
            return(user_choice)
        print_warning(f"Selection not valid. Select from {' or '.join(self.choices)}.")
        return(self.get_player_choice())

    # Computer's choice
    def get_computer_choice(self):
        return random.choice(self.choices)

    # Decide winner
    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return(print_warning("It's a tie!"))

        win_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return(print_success("Congratulations! You won!"))

        return(print_error("Oh no! You lost :( Better luck next time."))

    def play(self):
        user_choice = self.get_player_choice() 
        computer_choice = self.get_computer_choice()
        print(f'Computer choice: {computer_choice}')
        self.decide_winner(user_choice, computer_choice)


if __name__ == '__main__':
    game = RockPaperScissors('user')

    while True:
        game.play()

        continue_game = input("Press any key to play again, or press q to exit:\n")
        if continue_game.lower() == 'q':
            print_success_plain("See ya!")
            break