from util import CheckPrime

integer = int(input('Please enter a number : '))
print('Finding the Summation Prime of %s natural numbers' %(integer))
print('-------------------------------------------------')

i = 2
prime_numbers = []
while (i < integer):
    if(CheckPrime.isPrime(i)):
        prime_numbers.append(i)

    i+=1
    print('Checking Prime for : %s' %(i))

print('Prime Summation for numbers under %s : %s ' %(integer, sum(prime_numbers)))