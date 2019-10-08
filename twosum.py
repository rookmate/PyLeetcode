# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

result = "2019-10-08\nRuntime: 516 ms, faster than 40.57% of Python online submissions for Two Sum.\nMemory Usage: 12.5 MB, less than 94.52% of Python online submissions for Two Sum."


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in nums:
        second_elem = target - i
        try:
        # If it does not exist continues; Edge case where second is equal to first element;
            if nums.index(second_elem) or nums.index(second_elem) == 0:
                trim = list(nums)
                trim[trim.index(i)] = "a"
                return nums.index(i), trim.index(second_elem)
        except:
            continue


if __name__ == "__main__":
    twoSum([2, 7, 11, 15], 9)
    print(result)