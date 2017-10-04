i = 1
j = 2
k = 3

def isTriple(num1, num2, num3):
    return(num1**2 + num2**2 == num3**2)

def isSum1000(num1, num2, num3):
    return(num1 + num2 + num3 == 1000)

while not (isTriple(i,j,k) and isSum1000(i, j, k)):
    if(i < j-1):
        i+=1
    elif(j < k-1):
        i = 1
        j+=1
    else:
        i = 1
        j = 2
        k+=1

    print('Now Trying : %s %s %s' %(i,j,k))


print('Result Found : %s %s %s' %(i, j, k))
print('Result Product : %s ' %(i*j*k))
