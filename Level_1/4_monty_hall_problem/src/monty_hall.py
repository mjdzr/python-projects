import random


# Define the montyhall function with switch and stay options
def monty_hall(switch_doors: bool) -> bool:
    """Simulate one round of the Monty Hall problem.

    :param switch_doors: If True, the player switches their initial choice of door.
    :type switch_doors: bool
    :return: True if the player wins the car, False otherwise.
    :rtype: bool
    """
    # Define and shuffle doors
    doors = ['car'] + ['goat'] * 2
    random.shuffle(doors)

    # Define user's choice and the door revealed by Monty
    initial_choice = random.choice(range(len(doors)))
    doors_revealed = [i for i in range(len(doors)) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)

    # Return result based on user's choice
    if switch_doors:
        final_choice = [i for i in range(len(doors)) if i not in [initial_choice, door_revealed]][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'


def simulate_game(n_simulations: int, print: str = "ratio") -> tuple:
    """
    Simulate the Monty Hall game.

    :param n_simulations: Number of simulations to run
    :type n_simulations: int
    :param print: If "ratio", return the ratio of wins with and without switching.
                  If "count", return the count of wins with and without switching.
    :type print: str, optional
    :return: A tuple containing the results based on the specified print option
    :rtype: tuple
    """
    num_wins_with_switching = sum(monty_hall(switch_doors=True) for _ in range(n_simulations))
    num_wins_without_switching = sum(monty_hall(switch_doors=False) for _ in range(n_simulations))

    if print == "ratio":
        return num_wins_with_switching / n_simulations, num_wins_without_switching / n_simulations
    else:
        return num_wins_with_switching, num_wins_without_switching


if __name__ == "__main__":
    while True:
        try:
            n_simulations = int(input("Enter the number of simulations (positive integer): "))
            if n_simulations > 0:
                break
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        print_option = input("Enter the print option (ratio/count): ").strip().lower()
        if print_option in ["ratio", "count"]:
            break
        else:
            print("Invalid input. Please enter 'ratio' or 'count'.")

    results = simulate_game(n_simulations, print_option)
    if print_option == "ratio":
        print(f"Ratio of wins with switching: {results[0]:.2f}")
        print(f"Ratio of wins without switching: {results[1]:.2f}")
    else:
        print(f"Count of wins with switching: {results[0]}")
        print(f"Count of wins without switching: {results[1]}")