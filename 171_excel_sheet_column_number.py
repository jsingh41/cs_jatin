"""
171 Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/description/
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column_num = 0
        for i,letter in enumerate(s):
            column_num = 26 * column_num + ord(letter) - 64
        return column_num
            
