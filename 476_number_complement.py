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
        c = ''
        bin_c = ''
        bin_num = bin(num)[2:]
        print bin_num
        for i in range(0,len(bin_num)):
            print bin_num[i]
            if bin_num[i] == '0':
                # print bin_num[i]
                c = '1'
            elif bin_num[i] == '1':
                # print bin_num[i]
                c = '0'
            bin_c = bin_c+c
        print "bin output: ",(bin_c)
        return(int(bin_c,2))
        
