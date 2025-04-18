from termcolor import colored

# Define coloring functions
def print_success(msg, end = ""):
    print(colored(msg, color = 'black', on_color='on_green', attrs=['bold']), end=end)
def print_warning(msg, end = ""):
    print(colored(msg, color = 'black', on_color='on_yellow'), end=end)
def print_error(msg, end = ""):
    print(colored(msg, color = 'black', on_color='on_red'), end=end)
def print_grey(msg, end = ""):
    print(colored(msg, color = 'white', on_color='on_grey'), end=end)
def print_success_plain(msg, end = ""):
    print(colored(msg, color = 'green', attrs=['bold']), end=end)