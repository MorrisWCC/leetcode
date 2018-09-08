class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        rtn = 0
        for idx in range(0, len(nums), 2):
            rtn += nums[idx]
            
        return rtn