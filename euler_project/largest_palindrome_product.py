#!/usr/bin/env python
import sys
from util import CheckPalindrome

integer = int(sys.argv[1])
i = 2

result = 1
while i <= integer:
    j = 1
    while j <= integer:
        amount = i * j
        cp = CheckPalindrome
        if cp.isPalindrome(str(amount)) and amount > result:
            result = amount
        j += 1
    i += 1

print('Largest Palindrome product : %s' % result)
