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
        """
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table.pop(num)
            else:
                hash_table[num] = 1
        return hash_table.popitem()[0]
        """
        
        # Solution 3
        
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] = hash_table[num] + 1
            else:
                hash_table[num] = 1
        for key in hash_table:
            if hash_table[key] == 1:
                return key
                break
