"""
520 - Detect Capital
https://leetcode.com/problems/detect-capital/description/

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        sum_capital = 0
        if word[0].isupper():
            first_letter_upper = True
        else:
            first_letter_upper = False
        for i,letter in enumerate(word[1:]):
            if letter.isupper():
                sum_capital = sum_capital + 1
        if first_letter_upper:
            if sum_capital == len(word) - 1 or sum_capital == 0:
                return True
            else:
                return False
        elif not first_letter_upper:
            if sum_capital == 0:
                return True
            else:
                return False
