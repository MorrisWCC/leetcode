class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        """you can also use bin() and int() to easy get solution , but meanless"""
        
        len_a = len(a) - 1 
        len_b = len(b) - 1
        
        rtn = ""
        carry = 0
        
        while (len_a >= 0 or len_b >= 0) :
            if len_a >= 0 :
                carry += int(a[len_a])
                len_a -= 1
            if len_b >= 0 :
                carry += int(b[len_b])
                len_b -= 1

            rtn = str(carry%2) + rtn
            carry //= 2
        
        if carry == 1 :
            return "1"+rtn
        else :
            return rtn