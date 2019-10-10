# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


results = "2019-10-10\nRuntime: 4712 ms, faster than 19.84% of Python online submissions for Longest Palindromic Substring.\nMemory Usage: 20.4 MB, less than 17.81% of Python online submissions for Longest Palindromic Substring."


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    table = [[0 for x in range(length)] for y in range(length)]
    # boolean tabulation from dynamic programming to validade string indexes
    max_length = 1
    start_index = 0
    while (start_index < length):
        table[start_index][start_index] = True # all substrings of length 1 are palindromes
        start_index = start_index + 1

    reply_start = 0
    start_index = 0
    while start_index < length - 1:
        if (s[start_index] == s[start_index + 1]):
            table[start_index][start_index + 1] = True  # check for sub-string of length 2.
            reply_start = start_index
            max_length = 2
        start_index = start_index + 1


    substr_index = 3
    while substr_index <= length:                   # check for lengths greater than 2.
        start_index = 0                             # reset the starting index
        while start_index < (length - substr_index + 1):
        # get the ending index of substring from starting index start_index and length substr_index
            end_index  = start_index + substr_index - 1
            # s[start_index+1] to s[end_index-1] is a palindrome?
            if (table[start_index + 1][end_index  - 1] and s[start_index] == s[end_index ]):
                table[start_index][end_index] = True
                if (substr_index > max_length):     # reached longest size
                    reply_start = start_index
                    max_length = substr_index
            start_index = start_index + 1
        substr_index = substr_index + 1
    return s[reply_start : reply_start + max_length]


if __name__ == "__main__":
    print(list(map(longestPalindrome, ("babad", "cbbd", ""))))
    print(results)