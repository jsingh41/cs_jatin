"""
https://leetcode.com/problems/single-number-iii/description/
260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table.pop(num)
            else:
                hash_table[num] = 1
        return hash_table.keys()
        
