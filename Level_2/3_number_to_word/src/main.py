from constants import UNDER_20, TENS, ABOVE_100


def number_to_word(num: int) -> str:
    """
    Convert a number to its word representation.
    :param num: The number to convert (must be a non-negative integer).
    :return: The word representation of the number.

    # Example:
    >>> number_to_word(123)
    'one hundred twenty three'
    >>> number_to_word(1000)
    'one thousand'
    >>> number_to_word(1000000)
    'one million'
    """
    if num < 20:
        return UNDER_20[num]
    if num < 100:
        remainder = number_to_word(num % 10)
        if remainder == 'zero':
            return TENS[10 * (num // 10)]
        else:
            return TENS[10 * (num // 10)] + " " + remainder

    pivot = max(key for key in ABOVE_100 if num // key > 0)
    remainder = number_to_word(num % pivot)
    if remainder == 'zero':
        return f'{number_to_word(num // pivot)} {ABOVE_100[pivot]}'
    else:
        return f'{number_to_word(num // pivot)} {ABOVE_100[pivot]} {remainder}'

if __name__ == '__main__':
    # Convert to while loop to allow multiple inputs
    while True:
        try:
            user_input = input('Please enter a number in integer format to convert to word(s) or type "exit" to quit:\n')
            if user_input.lower() == 'exit':
                break
            # Check if input is a number
            num = float(user_input)
            # Check if input is positive
            if num < 0:
                raise ValueError("Number cannot be negative.")
            # Check if input is an integer
            if not num.is_integer():
                raise ValueError("Number must be an integer.")
            print(number_to_word(int(num)))
            user_retry = input('Try again? (yes/no):\n')
            if user_retry.lower()[0] != 'y':
                print("Exiting the program...")
                break
        except ValueError as e:
            print(f"Error: {e}")