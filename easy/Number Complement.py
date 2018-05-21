class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp_str = ""
        while num != 0 :
            if num & 1 == 1 :
                tmp_str = "0" + tmp_str
            else :
                tmp_str = "1" + tmp_str
                
            num = num >> 1
            
        return int(tmp_str, 2)