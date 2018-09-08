class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_split = A.split(' ')
        B_split = B.split(' ')
        all_word_dict = dict()
        rtn_set = set()
        for word in A_split:
            all_word_dict[word] = all_word_dict.get(word, 0) + 1
        for word in B_split:
            all_word_dict[word] = all_word_dict.get(word, 0) + 1
        
        for word, appear_times in all_word_dict.items():
            if appear_times == 1:
                rtn_set.add(word)
        
        return list(rtn_set) 
        
        