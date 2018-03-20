class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rtn = 0
        for num in nums :
            rtn ^= num
            
        return rtn