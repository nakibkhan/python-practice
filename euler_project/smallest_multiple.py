from util import check_lcm

number = int(input('Please enter a number : '))
print('Finding smallest number divisible by number between 1 and %s' % (number))
print('-------------------------------------------------')

mult_numbers = [i for i in range(1, number + 1)]
print(len(mult_numbers))

lcm = CheckLCM.find_lcm(mult_numbers[0], mult_numbers[1])

for i in range(2, len(mult_numbers)):
    lcm = CheckLCM.find_lcm(lcm, mult_numbers[i])

print('Result %s' % lcm)
