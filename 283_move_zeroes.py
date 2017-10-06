"""
283. Move Zeroes

https://leetcode.com/problems/move-zeroes/description/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        no_zero = False
        count_zeroes = 0
        while not no_zero:
            if 0 in nums:
                nums.remove(0)
                count_zeroes = count_zeroes + 1
            else:
                no_zero = True
        nums.extend([0] * count_zeroes)
        
        
            
        
        
        
