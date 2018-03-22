class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        _dict = {"]": "[" , ")":"(" , "}":"{" }
        
        for symbol in s :
            if symbol in _dict.values() :
                stack.append(symbol)
            else:
                if len(stack) == 0 or _dict[symbol] != stack.pop() :
                    return False
            
        else:
            return ( len(stack) == 0 )