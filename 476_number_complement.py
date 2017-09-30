"""
https://leetcode.com/problems/number-complement/description/
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Solution: Extract binary of the number using bin() function. For every character in the binary, get complement, append.
        binary_complement = ''
        bit_complement = ''
        binary_num = bin(num)[2:]
        for bit_char in binary_num:
            if bit_char == '0':
                bit_complement = '1'
            elif bit_char == '1':
                bit_complement = '0'
            binary_complement = binary_complement + bit_complement
        return int(binary_complement,2)
