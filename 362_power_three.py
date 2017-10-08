"""
362. Power of Three
https://leetcode.com/problems/power-of-three/description/
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        # All powers of 3 will have x as an integer where x = log n to the base 3
        log_n = math.log(n)/math.log(3)
        if float(log_n).is_integer():
            return True
            
        
