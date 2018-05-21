class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        len_S = len(S)
        c_idx_list = []
        rtn_list = []

        for idx, char in enumerate(S) :
            if char == C :
                c_idx_list.append(idx)
                
        for idx in range( 0, len_S ) :
            distance = 9999999
            for pos in c_idx_list :
                if abs(idx - pos) < distance :
                    distance = abs(idx - pos)
            rtn_list.append(distance)
            
        return rtn_list
                