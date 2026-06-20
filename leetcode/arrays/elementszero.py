def countValidSelections(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    indexes = [i for i, val in enumerate(nums) if val == 0]
    print (f"Indexes of 0s: {indexes}")

    for initdir in [1, -1]:
        workingarr = nums.copy()
        dir = initdir
        for i in indexes:
            j = i + dir
            for j in range(j, len(workingarr)):
                print(f"Current nums: {workingarr}, j: {j}, dir: {dir}, count: {count}")
                if all(num == 0 for num in workingarr):
                    count += 1
                    continue

                if workingarr[j] == 0:
                    j += dir

                if workingarr[j] > 0:
                    workingarr[j] -= 1
                    dir *= -1
                    j += dir


# Example usage:
nums = [0, 1, 1, 0, 1]
result = countValidSelections(None, nums)

