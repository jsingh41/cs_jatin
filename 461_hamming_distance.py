"""
https://leetcode.com/problems/hamming-distance/description/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        binary_x = bin(x)[2:]
        binary_y = bin(y)[2:]
        max_len = max(len(binary_x), len(binary_y))
        binary_x = binary_x.zfill(max_len)
        binary_y = binary_y.zfill(max_len)
        for i in range(0,max_len):
            if binary_x[i] != binary_y[i]:
                count = count + 1
        return count
        
