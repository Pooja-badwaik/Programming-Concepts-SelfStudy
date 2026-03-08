# 1. Given an unsorted list of integers nums, find the length of the longest consecutive
# sequence of elements. The algorithm should run in O(n) time
# Example:
# Input: [100,4,200,1,3,2]
# Output: 4






def longest_consecutive(nums):
    s = set(nums)   # store numbers in a set
    longest = 0

    for num in nums:
        if num - 1 not in s:   # start of a new sequence
            count = 1
            while num + count in s:
                count += 1
            longest = max(longest, count)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))