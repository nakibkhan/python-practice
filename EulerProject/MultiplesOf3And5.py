number = int(input('Please enter a number : '))
print('Finding all multiples of 3 and 5 below %s' %(number))
print('-------------------------------------------------')

i = 0
sum_list = []
while i < number:
    print('Try %s' %(i))
    if(i%3 == 0 or i%5 == 0):
        sum_list.append(i)
    i+=1

print('Total %s' %(sum(sum_list)))
