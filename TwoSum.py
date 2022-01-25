class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums = [2, 7, 11, 15]
        target = 9
        maps = {}

        for i, n in enumerate(nums):

            complement = target - nums[i]

            if complement in maps:
                return [maps[complement], i]

            maps[n] = i
