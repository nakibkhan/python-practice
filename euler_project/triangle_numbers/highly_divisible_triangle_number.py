from euler_project.util.check_all_factors import get_all_factors

def triangle_number(number):
    trinumber = 0
    while number > 1:
        trinumber += number
        number -= 1

    return trinumber + 1


def get_highly_divisible_triangle_number(divisor):
    n = 1
    d = 1

    while d < divisor:
        triangle_num = triangle_number(n)
        all_factors = get_all_factors(triangle_num)
        print(f'Triangle Number: {triangle_num}')
        print(f'All Factors: {all_factors}')

        d = len(all_factors)
        if d >= divisor:
            print(f'Triangle Number found : {triangle_num}')
        else:
            n +=1


if __name__ == "__main__":
    print("Finding Highly Divisible Triangle Number")
    divisor = 500
    print(f'Divisor Selected : {divisor}')
    get_highly_divisible_triangle_number(divisor)