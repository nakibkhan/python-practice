textFile = 'thousand_digit.txt'
numbers = []

def findGreatestProduct(line_numbers, result_list):
    start_index = 0
    end_index = 13
    product = []
    while end_index < len(line_numbers):
        result = 1
        index = start_index
        while index < end_index:
            result *= int(line_numbers[index])
            index += 1

        product.append(result)

        start_index += 1
        end_index += 1
    result_list.append(max(product))

with open(textFile) as fp:
    result_list = []
    file_nums = []
    for line in fp:
        line_nums = list(line.strip('\n'))
        file_nums.extend(line_nums)

    findGreatestProduct(file_nums, result_list)
    print(max(result_list))
