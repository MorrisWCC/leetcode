class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_arr = len(numbers)
        start = 0 
        end = len_arr - 1

        while start < end :
            tmp_sum = numbers[start] + numbers[end]
            if  tmp_sum == target :
                return [start+1,end+1]
            elif tmp_sum < target :
                start += 1
            else :
                end -= 1
        
        