def getPrimeFactors(number):
    """Returns a list of all factors

        Args:
            number: The number to check.

        Returns:
            The list of all factors for the number
        """
    all_factors = [1]

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            all_factors.append(i)

    all_factors.append(number)
    return all_factors


if __name__ == "__main__":
    print(getPrimeFactors(234))
