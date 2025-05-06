def is_happy(n: int):
    """
    A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.
    For example, 44 is a happy number because:
    4^2 + 4^2 = 16 + 16 = 32
    3^2 + 2^2 = 9 + 4 = 13
    1^2 + 3^2 = 1 + 9 = 10
    1^2 + 0^2 = 1 + 0 = 1

    Example:
    >>> is_happy(44)
    True
    >>> is_happy(32)
    False

    :param n: input number to check if it is a happy number
    :type n: int
    :return: True if the number is happy, False otherwise
    :rtype: bool
    """

    calculated_numbers = set()
    while (n != 1) and (n not in calculated_numbers):
        calculated_numbers.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1

if __name__ == '__main__':
    assert is_happy(44) is True
    assert is_happy(4) is False
    assert is_happy(32) is True
    assert is_happy(1) is True
    print("All tests passed!")