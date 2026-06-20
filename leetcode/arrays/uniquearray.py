import numpy as np

arr = np.array([3, 2, 4, 2, 3, 4, 1])

def findUniqueNumber(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

unq = findUniqueNumber(arr)
print(f"Unique number in Array: {unq}")