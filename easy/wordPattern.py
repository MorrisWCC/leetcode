class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        aux_dict = {}
        
        if len(pattern) != len(str_list) :
            return False
        
        for idx in range ( 0, len(pattern) ) :
            symbol = pattern[idx]
            if symbol not in aux_dict.keys() :
                if str_list[idx] not in aux_dict.values() :
                    aux_dict[symbol] = str_list[idx]
                
                else:
                    return False
            else :
                if str_list[idx] != aux_dict[symbol] :
                    return False
        else :
            return True