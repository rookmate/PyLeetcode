# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


results = "2019-10-10\nRuntime: 76 ms, faster than 70.30% of Python online submissions for Median of Two Sorted Arrays.\nMemory Usage: 11.9 MB, less than 65.96% of Python online submissions for Median of Two Sorted Arrays."


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    results_list = nums1+nums2
    results_list.sort()

    length = len(results_list)
    index = length // 2

    if length % 2 == 0:
        return (results_list[index -1] + results_list[index])/2.0
    else:
        return results_list[index]


if __name__ == "__main__":
    findMedianSortedArrays([1, 3], [2])
    findMedianSortedArrays([1, 2], [3, 4])
    print(results)