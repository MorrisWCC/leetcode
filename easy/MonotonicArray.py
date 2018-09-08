class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if len(A) <= 2:
            return True
        last_num = A[0]
        init_direction = -1
        direction = 0
        for num in A:
            if num == last_num:
                continue
            if num > last_num:
                direction = True
            else:
                direction = False
            
            if init_direction == -1:
                init_direction = direction
                
            if direction != init_direction:
                return False
            
            init_direction = direction
            last_num = num

        return True
        