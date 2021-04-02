# 15-4
# ----
# Given some words of various lengths, and a fixed number of characters that can be printed on a
# line, how can the words be printed to minimse white space at the end of each line? The words must
# retain their original ordering, but can be grouped together on any number of different lines as
# desired.

# Below is my solution, which uses dynamic programming, O(n^2) time and O(n^2) space.

import random

def minimise_extra_spaces(word_lengths, max_chars_per_line):
    n = len(word_lengths)
    if n == 0:
        return max_chars_per_line
    if max_chars_per_line < max(word_lengths):
        return None

    min_extra_spaces = [[float('inf') for __ in range(n)] for __ in range(n)]
    solution_reconstruction = [[-1 for __ in range(n)] for __ in range(n)]
    
    for l in range(0, n):
        for i in range(0, n-l):
            j = i + l
            extra_spaces_on_line = max_chars_per_line - l - sum(word_lengths[i:j+1])

            cur = extra_spaces_on_line if extra_spaces_on_line > 0 else float('inf')
            for m in range(i, j):
                spaces_with_split = min_extra_spaces[i][m] + min_extra_spaces[m+1][j]
                if spaces_with_split < cur:
                    cur = spaces_with_split
                    solution_reconstruction[i][j] = m

            min_extra_spaces[i][j] = cur

    print(display_solution(
        word_lengths, solution_reconstruction,
    ))
    return min_extra_spaces[0][n-1]

def display_solution(word_lengths, solution_reconstruction):
    return display_solution_helper(word_lengths, solution_reconstruction, 0, len(word_lengths)-1)
    
def display_solution_helper(word_lengths, solution_reconstruction, i, j):
    m = solution_reconstruction[i][j]
    if m == -1:
        return [word_lengths[i:j+1]]
    else:
        return (
            display_solution_helper(word_lengths, solution_reconstruction, i, m)
            + display_solution_helper(word_lengths, solution_reconstruction, m+1, j)
        )


num_words = random.randrange(0, 20)
word_lengths = [random.randrange(1, 12) for __ in range(num_words)]

max_chars_per_line = random.randrange(20, 100)


print(f'{word_lengths=}, {max_chars_per_line=}')
solution = minimise_extra_spaces(word_lengths, max_chars_per_line)
print(f'{solution=}')
