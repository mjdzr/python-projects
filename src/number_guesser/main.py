import random
from src.utils import print_error, print_grey, print_success, print_warning

# define the numeric function:
def check_number_type(s):
    try:
        s_int = int(s)
        if s_int < 1 or s_int > 100:
            print_error("Your number is not between 1 and 100; please try again", end="\n") 
            return False
        return True
    except ValueError:
        try:
            float(s)
            print_error("You have entered a number but in the float format; please provide an integer number without float point.", end="\n")
            return False

        except ValueError:
            print_error("You haven't entered a numeric value; please provide an integer value without float point and extra characters.", end="\n")
            return False

def main():
    random_num = random.randint(1, 100)
    # initialize the score
    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100 or press 'q' to quit: ")

        # Guess conditions
        if user_guess.lower() == 'q':
            print_grey("Thank you for playing. See ya!", end="\n")
            break

        if not check_number_type(user_guess):
            continue

        user_guess = int(user_guess)

        if random_num > user_guess:
            print_warning("Your guess is too low, please try again.", end="\n")
        elif random_num < user_guess:
            print_warning("Your guess is too high, please try again.", end="\n")
        else:
            print_success('Congratulations! You guess the right number!', end="\n")
            print_success(f'Your score is: {score}', end="\n")
            break

        score -= 10
        score = max(score, 0)

        if score == 0:
            print_error(f"Sorry! You lost the game! the number was {random_num}", end="\n")


if __name__ == '__main__':
    main()