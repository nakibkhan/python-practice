def getPrimeFactors(number):
    """Returns a list of prime factors

        Args:
            number: The number to check.

        Returns:
            The list of prime factors for the number
        """
    prime_factors = []
    i = 2
    while number != 1:
        if number % i == 0:
            prime_factors.append(i)
            number /= i
        else:
            if i == 2:
                i += 1
            else:
                i += 2

    return prime_factors
