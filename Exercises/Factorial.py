number = int(input("Please enter a number for finding the factorial of: "))

def findFactorial(integer):
    if(integer == 1):
        return 1
    else:
        return integer * findFactorial(integer - 1)

print '-------------------------------'
print 'Result : %s' %(findFactorial(number))
print '-------------------------------'
