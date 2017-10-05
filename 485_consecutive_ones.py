"""
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/description/

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        overall_sum = 0
        for i,num in enumerate(nums):
            if num == 1:
                sums = sums + 1
                if sums > overall_sum:
                    overall_sum = sums
            else:
                sums = 0
        return overall_sum
