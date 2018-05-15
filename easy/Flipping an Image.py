class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        len_A = len(A)
        rtn_list = []
        
        for data in A :
            data.reverse()
            tmp = []
            for digit in data :
                digit = digit ^ 1
                tmp.append(digit)
            rtn_list.append(tmp)
        return rtn_list