textFile = 'thousand_digit.txt'
numbers = []
with open(textFile) as fp:
    for line in fp:
        line_nums = list(line.strip('\n'))
        numbers.extend(line_nums)

max_product = 0
i = 0
size_adjacent = 13

def findProduct(result,list, index):
    if(integer == 1):
        return 1
    else:
        return integer * findFactorial(integer - 1)

while(len(numbers) > (i+size_adjacent-1)) :
    print