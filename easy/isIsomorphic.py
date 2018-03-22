class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        len_str = len(s)
        
        for idx in range ( 0, len_str ) :
            num_in_s = dict_s.get(s[idx],0)
            num_in_t = dict_t.get(t[idx],0)
            
            if num_in_s != num_in_t :
                return False
            
            dict_s[s[idx]] = dict_s.get(s[idx],1) + idx
            dict_t[t[idx]] = dict_t.get(t[idx],1) + idx
        else :
            return True
            
        