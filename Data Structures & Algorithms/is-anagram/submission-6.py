class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Goal in 1-2 plain sentences -> Return True IF anagram ELSE False
        """

        # 1. Counter(s) == Counter(t) <-> Dictonary/HashMap
        # 2. Frequency Counter = List & Dict
        # List is better if the character set is limited. List Character Count 

        return Counter(s) == Counter(t)

        