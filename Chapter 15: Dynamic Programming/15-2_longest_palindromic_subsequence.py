# 15-2
# ----
# Given a string s, find the longest palindromic subsequence of s. For instance, if
# s = 'hello there' then the longest palindromic substring of s is 'elle', so the function should
# return 4.

# Below is my solution, which uses dynamic programming and runs in O(n^2) time using O(n^2) space.

def longest_pal_sub(s):
    n = len(s)
    if n == 0:
        return 0

    partial_lps = [[1 for __ in range(n)] for __ in range(n)]

    for i in range(n-1):
        partial_lps[i][i+1] = 1 + int(s[i] == s[i+1])

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            if s[i] == s[j]:
                partial_lps[i][j] = partial_lps[i+1][j-1] + 2
            else:
                partial_lps[i][j] = max(partial_lps[i][j-1], partial_lps[i+1][j])
    
    return partial_lps[0][n-1]


w = 'hello there'
m = longest_pal_sub(w)
print(m)
