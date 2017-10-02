class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1 : To find non-repeating value:  2 * (a+b+c) - (a+a+b+c+c) = b
        # O(n)
        """
        unique_values_nums = set(nums)
        return 2 * sum(unique_values_nums) - sum(nums)
        """
        
        # Solution 2 : Create hash table and pop
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
