class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Goal in 1-2 plain sentences -> Return True IF anagram ELSE False
        """

        # 1. Counter(s) == Counter(t) <-> Dictonary/HashMap 
        # 2. Frequency Counter = List & Dict
        # List is better if the character set is limited. List Character Count

        if len(s) != len(t):
            return False

        # character counter - list 
        count = [0] * 26

        # check if it can be optimised using zip or enumerate
        for i in range(len(s)): 
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # return False if any value in count != 0
        # research about more pythonic way of doing this
        for c in count:
            if c != 0: 
                return False
        
        return True






        