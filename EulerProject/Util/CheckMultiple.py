def isMultipleOfThree(number):
    listNum = [int(d) for d in str(number)]
    if(sum(listNum) %3 == 0):
        return True
    return False

def isMultipleOfFive(number):
    listNum= [int(d) for d in str(number)]

    if(listNum[len(listNum) - 1] in [0, 5]):
        return True
    return False

def isMultipleOfNine(number):
    listNum = [int(d) for d in str(number)]
    if(sum(listNum) %9 == 0):
        return True
    return False

def isEven(number):
    return(number%2 == 0)