# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


results = "2019-10-10\nRuntime: 44 ms, faster than 99.32% of Python online submissions for Longest Palindromic Substring.\nMemory Usage: 11.8 MB, less than 61.64% of Python online submissions for Longest Palindromic Substring."


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s

    max_length = 0
    start_index = 0
    length = len(s)
    print(s)
    for index in range(length):
        # EVEN SIZE STRING -> index-max_length
        if s[index-max_length:index+1] == s[index-max_length:index+1][::-1]:
            start_index = index - max_length
            max_length = max_length + 1
        # ODD SIZE STRING -> index-max_length-1
        if index >= max_length + 1 and s[index-max_length-1:index+1] == s[index-max_length-1:index+1][::-1]:
            start_index = index - max_length - 1
            max_length = max_length + 2

    return s[start_index : start_index + max_length]


if __name__ == "__main__":
    print(list(map(longestPalindrome, ("babad", "cbbd", "", "aba", "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))))
    print(results)