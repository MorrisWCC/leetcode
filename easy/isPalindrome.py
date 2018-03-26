class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        
        start = 0
        end = len(s)-1
        s = s.lower()

        while start < end :
            if ( not s[start].isalnum() ) :
                start += 1
                continue
            if ( not s[end].isalnum() ) :
                end   -= 1
                continue

            if s[start] == s[end] :
                start += 1
                end -= 1
            else:
                return False
            
        return True
            
            
            