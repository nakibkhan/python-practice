#!/usr/bin/env python
from util import check_prime

number = int(input('Please enter a number : '))
print('Finding %s-th Prime Number ' %(number))
print('-------------------------------------------------')

i = 1
result = 2
while(i < number):
    result+=1
    if(CheckPrime.isPrime(result)):
        i+=1
        print('The %s-th Prime Number is : %s ' % (i, result))


print('The %s-th Prime Number is : %s ' %(i, result))