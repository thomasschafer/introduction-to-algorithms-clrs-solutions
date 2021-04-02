# 15.4-5
# ------
# Find the longest monotonically increasing subsequence of a sequence of numbers.

# Below is my solution, which uses dynamic programming and runs in O(n^2) time using O(n) space.

import random

def length_of_LMIS_with_solution(nums):
    n = len(nums)
    partial_sizes = [1] * n if n != 0 else [0]
    prev_indices = [None] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if  partial_sizes[j] + 1 > partial_sizes[i]:
                    partial_sizes[i] = partial_sizes[j] + 1
                    prev_indices[i] = j

    print(reconstruct_solution(nums, partial_sizes, prev_indices))

    return max(partial_sizes)

def reconstruct_solution(nums, partial_sizes, prev_indices):
    if nums == []:
        return []

    cur = partial_sizes.index(max(partial_sizes))
    solution = []

    while cur is not None:
        solution = [nums[cur]] + solution
        cur = prev_indices[cur]

    return solution


length = random.randrange(0, 20)
x = [random.randrange(-10, 10) for __ in range(length)]

print(x)
print(length_of_LMIS_with_solution(x))