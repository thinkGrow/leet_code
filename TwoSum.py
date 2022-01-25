'''
Problem Link : https://leetcode.com/problems/two-sum/

Runtime: 49 ms, faster than 73.49% of Python online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 72.74% of Python online submissions for Two Sum.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        maps = {}

        for i, n in enumerate(nums):

            complement = target - nums[i]

            if complement in maps:
                return [maps[complement], i]

            maps[n] = i
