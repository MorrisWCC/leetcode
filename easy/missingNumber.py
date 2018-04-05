class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        origin_sum = sum(nums)
        suppose_sum = ( len(nums)+1 ) * len( nums ) // 2
        
        return suppose_sum - origin_sum