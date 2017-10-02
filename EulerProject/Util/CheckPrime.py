def isPrime(number):
    if(number == 2):
        return True
    i = 2
    while (i <= number/2):
        if(number % i == 0):
            return False
        i+=1
    print('------------------------------------------------')
    print('\t\t\t %s is a Prime Number' %(number))
    print('------------------------------------------------')
    return True