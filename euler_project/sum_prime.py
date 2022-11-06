#!/usr/bin/env python
from util import CheckPrime

number = int(input('Please enter a number : '))
print('Finding Sum Primes below %s' %(number))
print('-------------------------------------------------')

result = 2
total = result
while(result < number):
    result+=1
    if(CheckPrime.isPrime(result)):
        print('%s is a Prime Number.' %(result))
        total+=result

print('The total sum for prime numbers below %s is : %s ' %(number, total))