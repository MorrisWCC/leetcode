class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        comparator = 1
        while comparator < num :
            comparator = comparator << 2
        
        return comparator == num