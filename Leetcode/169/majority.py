# 169. Majority Element
# Easy
# 17.6K
# 529
# Companies

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

 

# Constraints:

#     n == nums.length
#     1 <= n <= 5 * 104
#     -109 <= nums[i] <= 109

 
# Follow-up: Could you solve the problem in linear time and in O(1) space?

# The Easy Way:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        midpoint = len(nums) // 2 + len(nums) % 2
        return sorted(nums)[midpoint - 1]

# The Hard Way:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return nums[0]
        
        lookup = {}
        count = 0
        max_count = 0
        idx = 0

        for num in nums:
            count = lookup.get(num, 0) + 1
            if count > max_count:
              max_count = count
              
            lookup[num] = count

        return num 
