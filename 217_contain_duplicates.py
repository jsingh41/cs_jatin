"""
https://leetcode.com/problems/contains-duplicate/description/

Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, and it should return false if every element
is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictionary = {}
        duplicates = []
        is_duplicate = False
        for num in nums:
            if num in dictionary:
                return True
                is_duplicate = True
                break
            else:
                dictionary[num] = 1
        return is_duplicate
        
        
