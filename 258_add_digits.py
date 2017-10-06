"""
258. Add Digits
https://leetcode.com/problems/add-digits/description/

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        # Recursive solution
        s = Solution()
        sum_digits = 0
        if num < 10:
            return num
        else:   
            sum_digits = sum_digits + int(num % 10) + s.addDigits(int(num/10))
        if sum_digits > 9:
            sum_digits = s.addDigits(sum_digits)
        return sum_digits
        """
        
        # O(1) solution. (See https://en.wikipedia.org/wiki/Digital_root)
        if num > 0:
            return num - 9 * int((num - 1) / 9)
        else:
            return 0
        
        
