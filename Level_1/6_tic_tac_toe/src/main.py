import random

import numpy as np


class TicTacToe:
    def __init__(self):
        self.board = ['   '] * 10 # first index is ignored
        self.turn = self.get_random_first_player()

    # Define who starts first
    def get_random_first_player(self):
        choice = random.choice(['X', 'O'])
        return choice

    def show_board(self):
        print('\n')
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-----------')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-----------')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print('\n')

    # Swap player
    def swap_player(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    # Define is board full
    def is_board_full(self):
        # Ignore index 0, only check cells 1-9
        return all(cell != '   ' for cell in self.board[1:])

    # Define mark the spot
    def mark_spot(self, player, cell):
        self.board[cell] = f' {player} '

    # Define has player won
    def has_player_won(self, player):
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
            [1, 5, 9], [3, 5, 7] # diagonal
        ]

        for combination in win_combinations:
            if all(self.board[cell] == f' {player} ' for cell in combination):
                return True

        return False

    # Start the game
    def start(self):
        while True:
            self.show_board()
            print(f'Player {self.turn} turn!')

            # get user's input. If it's not numeric, keep trying to get user's input
            # If the input is not between 1 and 9 and or cell is not empty, keep trying to get user's input
            # If the input can be converted to numeric, keep trying to get user's input
            while True:
                try:
                    cell = int(input('Choose a cell (1-9):\n'))
                    if cell < 1 or cell > 9:
                        print('Invalid input. Please choose a number between 1 and 9.')
                        continue
                    if self.board[cell] != '   ':
                        print('Cell already taken. Please choose another cell.')
                        continue
                    break
                except ValueError:
                    print('Invalid input. Please enter a number between 1 and 9.')

            # mark the spot
            self.mark_spot(self.turn, cell)

            # Has player won?
            if self.has_player_won(self.turn):
                self.show_board()
                print(f'Player {self.turn} wins!')
                return

            # Is the board full?
            if self.is_board_full():
                print('Game over! It\'s a tie!')
                self.show_board()
                return

            # Swap player
            self.swap_player()

if __name__ == '__main__':
    game = TicTacToe()
    game.start()