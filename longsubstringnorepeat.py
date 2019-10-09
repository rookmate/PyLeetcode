# Given a string, find the length of the longest substring without repeating characters.

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

result = "2019-01-09\nRuntime: 32 ms, faster than 96.29% of Python online submissions for Longest Substring Without Repeating Characters.\nMemory Usage: 12 MB, less than 67.19% of Python online submissions for Longest Substring Without Repeating Characters."


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:               # if empty string leave
        return 0

    start = 0               # start index in string
    maxLength = 0           # start as no length
    usedChars = {}          # dictionary/hashtable of used chars
    curr_index = 0          # character current index in string

    for char in s:
    # if already used and start index < current longest substring size, starts searching for new one
        if char in usedChars and start <= usedChars[char]:
            start = usedChars[char]
        else:  # compares previous max with current max
            maxLength = max(maxLength, curr_index - start + 1)
        # updates index and amount of used characters
        curr_index += 1
        usedChars[char] = curr_index
    return maxLength

if __name__ == "__main__":
    print(list(map(lengthOfLongestSubstring, ("abcabcbb", "bbbbb", "pwwkew"))))
    print(result)