class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        rtn_list = [0] * len(temperatures)
        stack = list()
        for idx, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                top = stack.pop()
                rtn_list[top] = idx - top
            stack.append(idx)
            
        return rtn_list
        