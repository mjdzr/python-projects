import pandas as pd
from termcolor import colored

# Define word freqnency function
def generate_word_frequency(my_file, word_len: int = 5, limit: int = 1000, 
                            word_col = "word", count_col = "count"):
    filtered_df = my_file[my_file[word_col].str.len() == word_len]
    sorted_df = filtered_df.sort_values(by=count_col, ascending=False)
    truncated_df = sorted_df[:limit][word_col].unique()
    return(list(truncated_df))

# Define coloring functions
def print_success(msg, end = ""):
    print(colored(msg, color = 'black', on_color='on_green', attrs=['bold']), end=end)
def print_warning(msg, end = ""):
    print(colored(msg, color = 'black', on_color='on_yellow'), end=end)
def print_error(msg, end = ""):
    print(colored(msg, color = 'black', on_color='on_red'), end=end)
def print_grey(msg, end = ""):
    print(colored(msg, color = 'white', on_color='on_grey'), end=end)