import pandas as pd
from src.utils import print_error, print_grey, print_success, print_warning
import random

class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10_000,
                 word_col = "word", count_col = "count"):
        self.word_len = word_len
        self.words = self.generate_word_frequency(file_path, word_len, limit, word_col, count_col)

    # Define word freqnency function
    def generate_word_frequency(self, file_path, word_len, limit, word_col, count_col):
        my_file = pd.read_csv(file_path)

        # Make the word_col upper case
        my_file[word_col] = my_file[word_col].str.upper()

        # Filter the DataFrame based on word length
        filtered_df = my_file[my_file[word_col].str.len() == word_len]

        # Sort the DataFrame by count column in descending order and truncate to limit
        sorted_df = filtered_df.sort_values(by=count_col, ascending=False)
        truncated_df = sorted_df[:limit][word_col].unique()

        # Convert to list
        return(list(truncated_df))



    def run(self, ):

        # Get the random word
        word = random.choice(self.words)

        print(word)

        # Get user's guess
        num_guesses = 0
        max_guesses = 6

        while(True):
            guess_word = input(f'Enter a {self.word_len} letter word or "q" to exit: ')
            guess_word = guess_word.upper()

            # Chicken
            if guess_word == 'Q':
                break

            # Check number of letters
            if len(guess_word) != self.word_len:
                print_grey(f'Number of letters is not {self.word_len}. Try again!', end = "\n")
                continue

            # Check if the word is in the list
            if guess_word not in self.words:
                print_grey(f'{guess_word} is not in our word list. Try again!', end = "\n")
                continue

            # Check if the word is correct
            for w_letter, guess_letter in zip(word, guess_word):
                if w_letter == guess_letter:
                    print_success(f' {guess_letter} ')
                    print(' ', end="")
                elif guess_letter in word:
                    print_warning(f' {guess_letter} ')
                    print(' ', end="")
                else:
                    print_error(f' {guess_letter} ')
                    print(' ', end="")

            # Print full success
            if guess_word == word:
                print_success(f'\nCongratulations! You guessed the word {word} in {num_guesses + 1} guesses.')
                break

            # Final checks
            num_guesses += 1
            if num_guesses > max_guesses:
                print_warning(f'\nYou are out of guesses! The word was {word}.\n')
                break
            print_grey(f'\n{max_guesses - num_guesses + 1} guesses remaining.\n')

# if __name__ == '__main__':
#     wordle = Wordle()
#     wordle.run()