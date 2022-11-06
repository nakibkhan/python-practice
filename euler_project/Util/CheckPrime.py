import math


def isPrime(number):
    """Checks whether the number is a prime number.

        Args:
            number: The number to check.

        Returns:
            A boolean value on whether the argument is a prime number or not.
        """
    if number == 2:
        return True
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True
