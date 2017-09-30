"""
https://leetcode.com/problems/judge-route-circle/description/

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        # Solution: x and y hold distance moved from origin. Final x and y should be 0,0
        for i in range(0,len(moves)):
            if moves[i] == 'L':
                x = x - 1
            if moves[i] == 'R':
                x = x + 1
            if moves[i] == 'U':
                y = y + 1
            if moves[i] == 'D':
                y = y - 1
            i = i + 1
        return(x==0 and y==0)
