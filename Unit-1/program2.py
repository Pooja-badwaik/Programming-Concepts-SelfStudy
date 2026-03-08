
# 2. Given a list of integers nums, return a list output such that output[i] is equal to the
# product of all the elements in nums except nums[i]. You must solve it without using division
# and in O(n) time.
# Example:
# Input: [1,2,3,4]
# Output: [24,12,8,6]


nums = [1, 2, 3, 4]
output = []

for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
        if i != j:
            product = product * nums[j]
    output.append(product)

print(output)