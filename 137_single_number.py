"""
https://leetcode.com/problems/single-number-ii/description/
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # For no extra memory, we'll go with the pop method
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] = hash_table[num] + 1
            else:
                hash_table[num] = 1
        for key in hash_table:
            if hash_table[key] == 1:
                return key
                break
            
        
