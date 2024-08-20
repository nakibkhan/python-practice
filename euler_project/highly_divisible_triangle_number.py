#!/usr/bin/env python
import sys
from util import check_all_factors as checkFactors


def triangleNumber(number):
    trinumber = 0
    while number > 1:
        trinumber += number
        number -= 1

    return trinumber + 1


if __name__ == "__main__":
    index = 500000
    result = 1

    while len(checkFactors.getPrimeFactors(result)) <= 500:
        index += 1
        print(index)
        result = triangleNumber(index)
        print(result)
    print(result)
