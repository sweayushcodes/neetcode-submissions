class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26

        for char in s: 
            counts[ord(char.lower()) - ord('a')] += 1

        for char in t: 
            counts[ord(char.lower()) - ord('a')] -= 1

        return all(count == 0 for count in counts)