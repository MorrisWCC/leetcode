class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        aux_dict = {}
        len_nums = len(nums)
        
        for idx in range( len_nums - 1) :
            aux_dict[nums[idx]] = idx
            if nums[idx+1] in aux_dict :
                if (idx+1) - aux_dict[nums[idx+1]] <= k :
                    return True
        else:
            return False