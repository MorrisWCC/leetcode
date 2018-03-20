class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_of_zero = 0
        move_idx = 0
        for idx in range ( 0, len(nums)) :
            if nums[idx] != 0 :
                nums[move_idx] = nums[idx]
                move_idx += 1
            else :
                num_of_zero += 1
        
        for idx in range ( 0, num_of_zero ) :
            nums[move_idx] = 0
            move_idx += 1