class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {num : idx for (idx, num) in enumerate(nums)}
        
        for (idx, num) in enumerate(nums):
            new_target = target - num
            if new_target in d and idx != d[new_target]:
                return [idx, d[new_target]]
