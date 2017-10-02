from Util import CheckPrime

integer = int(input('Please enter a number : '))
print('Finding the largest Prime Factor of %s' %(integer))
print('-------------------------------------------------')

prime_factors = []
def findPrimeFactors(number):
    if (number % 2 == 0):
        prime_factors.append(2)
    if(number >= 3):
        i = 3
        while (i <= number/2):
            if(number%i == 0 and CheckPrime.isPrime(i)):
                print('---------------------------------------------------------------------')
                print('\t\t\t\t Prime Factor found %s' %(i))
                print('---------------------------------------------------------------------')
                prime_factors.append(i)
            i+=1
            print('Check Prime for number %s' %(i))

findPrimeFactors(integer)

print('Prime Factors for %s are : %s' %(integer, prime_factors))