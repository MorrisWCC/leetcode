class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        total_widths = 0
        rtnList = list()
        remain_space = 100
        total_line = 1
        for letter in S:
            letter_width = widths[ord(letter)-ord('a')]
            if remain_space >= letter_width:
                remain_space -= letter_width
            else:
                total_line += 1
                remain_space = 100 - letter_width
        
        rtnList.append(total_line)
        rtnList.append(100-remain_space)
        return rtnList
        