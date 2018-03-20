class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtn_list = []

        for num in range ( n, 0, -1 ) :
            if num % 15 == 0 :
                rtn_list.append("FizzBuzz")
            elif num % 5 == 0 :
                rtn_list.append("Buzz")
            elif num % 3 == 0 :
                rtn_list.append("Fizz")
            else :
                rtn_list.append(str(num))
                
        return rtn_list[::-1]