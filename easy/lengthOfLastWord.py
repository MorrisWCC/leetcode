class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        spilt_list = s.split()
        len_s_l = len(spilt_list)
        if len_s_l == 0 :
            return 0
        
        return len(spilt_list[len_s_l-1])