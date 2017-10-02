integer = int(input('Please enter a number : '))
print('Finding the Sum Square Difference of %s' %(integer))
print('-------------------------------------------------')


def squareSum(number):
    if(number == 1):
        return 1

    i= 1
    result = []
    while i <=number:
        result.append(i*i)
        i+=1
    return sum(result)

def sumSquare(number):
    if (number == 1):
        return 1
    i = 1
    result = 0
    while i <=number:
        result+=i
        i+=1
    return result ** 2

print('The Sum Square Difference of %s is : %s' %(integer, sumSquare(integer) - (squareSum(integer))))