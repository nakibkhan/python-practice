print('Finding all even Fibonacci Numbers')
print('-------------------------------------------------')

def fibNum(integer):
    if(integer == 1):
        return 1
    if(integer == 2):
        return 2
    return fibNum(integer - 1) + fibNum(integer - 2)

sum_list = []

i = 1
result = 0

while result < 4000000:
    result = fibNum(i)
    i+=1
    if(result %2 == 0):
        print('Even Fibonacci Number : %s' %(result))
        sum_list.append(result)
print('Fibonacci Number Limit 4000000 reached')

print('Sum of Fib Numbers : %s' %(sum(sum_list)))