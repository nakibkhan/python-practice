#!/usr/bin/env python
"""Returns a list of all the Prime Factors for a number.

Usage:
    python LargestPrimeFactor.py <number>

    example: python LargestPrimeFactor.py 3456789
"""
import math
import sys
from Util import CheckPrime

integer = int(sys.argv[1])

prime_factors = []
def findPrimeFactors(number):
    if (number % 2 == 0):
        prime_factors.append(2)
    if(number >= 3):
        i = 3
        while (i <= math.sqrt(number)):
            if(number%i == 0 and CheckPrime.isPrime(i)):
                print('%s is a Prime number for %s' %(i, number))
                prime_factors.append(i)
            i+=2

findPrimeFactors(integer)

print('Prime Factors for %s are : %s' %(integer, prime_factors))