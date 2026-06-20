import math


def getPrimeFactors(number):
    """Returns a list of prime factors

        Args:
            number: The number to check.

        Returns:
            The list of prime factors for the number
        """
    prime_factors = []

    while number % 2 == 0:
        number /= 2
        prime_factors.append(2)

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(i)
            number /= i

    if number > 2:
        prime_factors.append(number)

    return prime_factors

