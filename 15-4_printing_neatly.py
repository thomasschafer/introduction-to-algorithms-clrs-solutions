#15-4

import random
import numpy as np


def minimise_extra_spaces(word_lengths, max_chars_per_line):
    n = len(word_lengths)
    min_extra_spaces = [[float('inf') for __ in range(n)] for __ in range(n)]
    solution_reconstruction = [[None for __ in range(n)] for __ in range(n)]
    
    for l in range(0, n):
        for i in range(0, n-l):
            j = i + l
            extra_spaces_on_line = max_chars_per_line - l - sum(word_lengths[i:j+1])

            cur = extra_spaces_on_line if extra_spaces_on_line > 0 else float('inf')
            for m in range(i, j):
                cur = min(cur, min_extra_spaces[i][m] + min_extra_spaces[m+1][j])

            min_extra_spaces[i][j] = cur

    print(np.array(min_extra_spaces))
    return min_extra_spaces[0][n-1]


# num_words = random.randrange(0, 20)
# word_lengths = [random.randrange(1, 12) for __ in range(num_words)]

# max_chars_per_line = random.randrange(20, 100)

word_lengths=[3, 2, 4, 6, 7]
max_chars_per_line=8

print(f'{word_lengths=}, {max_chars_per_line=}')
print(minimise_extra_spaces(word_lengths, max_chars_per_line))
