# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


results = "2019-10-10\nRuntime: 5912 ms, faster than 8.96% of Python online submissions for Longest Palindromic Substring.\nMemory Usage: 11.9 MB, less than 60.27% of Python online submissions for Longest Palindromic Substring."


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s

    max_length = 1
    start_index = 0
    length = len(s)
    for index in range(length):
        inc_index = index + 1
        while inc_index <= length and max_length <= length - index:
            # If substring s[index : inc_index] is a palindrome and longer than current max length
            if s[index : inc_index] == s[index : inc_index][::-1] and inc_index - index > max_length:
                start_index = index
                max_length = inc_index - index
            inc_index += 1
    return s[start_index : start_index + max_length]


if __name__ == "__main__":
    print(list(map(longestPalindrome, ("babad", "cbbd", "", "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))))
    print(results)