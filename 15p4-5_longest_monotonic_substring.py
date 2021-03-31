#15.4-5

import random

# def longest_monotonic_subs(nums):
#     if nums == []:
#         return 0
    
#     n = len(nums)
#     partial_lms_sizes = [1] * n
#     reconstruct_indices = [None] * n

#     for i in range(n):
#         max_partial_lms = 1
#         prev_index = None
#         for j in range(0, i):
#             if nums[j] < nums[i]:
#                 if partial_lms_sizes[j] + 1 > max_partial_lms:
#                     max_partial_lms = partial_lms_sizes[j] + 1
#                     prev_index = j

#         partial_lms_sizes[i] = max_partial_lms
#         reconstruct_indices[i] = prev_index
#     return partial_lms_sizes, reconstruct_indices

# def reconstruct_lms(partial_lms_sizes, reconstruct_indices):
#     cur = len(partial_lms_sizes) - 1
#     solution = []

#     while reconstruct_indices[cur] is not None:
#         prev = reconstruct_indices[cur]
#         if (not prev) or partial_lms_sizes[cur] > partial_lms_sizes[prev]:
#             solution = [cur] + solution
#         cur = prev

#     solution = [cur] + solution

#     return solution


def reconstruct_solution(nums, partial_sizes, prev_indices):
    if nums == []:
        return []

    cur = partial_sizes.index(max(partial_sizes))
    solution = []

    while cur is not None:
        solution = [nums[cur]] + solution
        cur = prev_indices[cur]

    return solution

def length_of_LIS_with_solution(nums):
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

length = random.randrange(0, 20)
x = [random.randrange(-10, 10) for __ in range(length)]

# print(x)
# partial_lms_sizes, reconstruct_indices = longest_monotonic_subs(x)
# print(f'{partial_lms_sizes=}')
# print(f'{reconstruct_indices=}')
# print(max(partial_lms_sizes), pure_longest_monotonic_subs(x))
# soln = reconstruct_lms(partial_lms_sizes, reconstruct_indices)
# # print(soln)
# print([x[i] for i in soln])

print(x)
print(length_of_LIS_with_solution(x))