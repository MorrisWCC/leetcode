class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rtn_list = []
        for num in nums :
            if nums[abs(num)-1] > 0 :
                nums[abs(num)-1] *= -1
        
        for idx in range(0,len(nums)) :
            if nums[idx] > 0 :
                rtn_list.append(idx+1)
                
        return rtn_list