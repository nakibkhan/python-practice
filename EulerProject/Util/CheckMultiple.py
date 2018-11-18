def isMultipleOfThree(number):
    """Checks if value is multiple of 3.

            Args:
                number: Number to check.

            Returns:
                Returns a boolean on whether the number is multiple of 3.
            """
    listNum = [int(d) for d in str(number)]
    if(sum(listNum) %3 == 0):
        return True
    return False

def isMultipleOfFive(number):
    """Checks if value is multiple of 5.

            Args:
                number: Number to check.

            Returns:
                Returns a boolean on whether the number is multiple of 5.
            """
    listNum= [int(d) for d in str(number)]

    if(listNum[len(listNum) - 1] in [0, 5]):
        return True
    return False

def isMultipleOfNine(number):
    """Checks if value is multiple of 9.

            Args:
                number: Number to check.

            Returns:
                Returns a boolean on whether the number is multiple of 9.
            """
    listNum = [int(d) for d in str(number)]
    if(sum(listNum) %9 == 0):
        return True
    return False

def isEven(number):
    """Checks if value is an even number.

            Args:
                number: Number to check.

            Returns:
                Returns a boolean on whether the number is even or not.
            """
    return(number%2 == 0)