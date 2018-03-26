class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start = 0 
        end = int( c ** (0.5) )
        
        while start <= end :
            value = start**2 + end**2
            if value < c :
                start += 1
            elif value > c :
                end   -= 1
            else :
                return True
            
        return False