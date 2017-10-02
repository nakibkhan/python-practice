from Util import CheckPalindrome

integer = int(input('Please enter a number : '))
print('Finding the largest Palidrome Product of %s' %(integer))
print('-------------------------------------------------')

i = 2

result = 1
while(i < integer):
    j = 1
    while(j <= i):
        amount = i * j
        if (CheckPalindrome.isPalindrome(str(amount)) and amount > result):
            result = amount
        j+=1
    i+=1

print('Largest Palindrome product : %s' %(result))

