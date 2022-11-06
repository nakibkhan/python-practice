textFile = 'grid.txt'


def prod_backslash(num_list):
    j = 0
    result_list = []

    while j < 17:
        i = 0
        while i < 17:
            product_result = int(num_list[i][j]) * int(num_list[i + 1][j + 1]) * int(num_list[i + 2][j + 2]) * int(
                num_list[i + 3][j + 3])
            result_list.append(product_result)
            i += 1
        j += 1

    return result_list


def prod_frontslash(num_list):
    j = 0
    result_list = []

    while j < 17:
        i = 3
        while i < 20:
            product_result = int(num_list[i][j]) * int(num_list[i - 1][j + 1]) * int(num_list[i - 2][j + 2]) * int(
                num_list[i - 3][j + 3])
            result_list.append(product_result)
            i += 1
        j += 1

    return result_list

def prod_topdown(num_list):
    j = 0
    result_list = []

    while j < 17:
        i = 0
        while i < 20:
            product_result = int(num_list[i][j]) * int(num_list[i][j + 1]) * int(num_list[i][j + 2]) * int(
                num_list[i][j + 3])
            result_list.append(product_result)
            i += 1
        j += 1

    return result_list

def prod_leftright(num_list):
    j = 0
    result_list = []

    while j < 20:
        i = 0
        while i < 17:
            product_result = int(num_list[i][j]) * int(num_list[i + 1][j]) * int(num_list[i + 2][j]) * int(
                num_list[i + 3][j])
            result_list.append(product_result)
            i += 1
        j += 1

    return result_list

with open(textFile) as fp:
    product_list = []
    file_nums = []
    for line in fp:
        file_nums.append(line.strip('\n').split(" "))
    product_list.extend(prod_backslash(file_nums))
    product_list.extend(prod_frontslash(file_nums))
    product_list.extend(prod_topdown(file_nums))
    product_list.extend(prod_leftright(file_nums))

    print(max(product_list))