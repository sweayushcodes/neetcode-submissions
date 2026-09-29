class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can you use string as a key in maps?? 
        # is it hashed when stored & used as a key? 
        # 

        res = defaultdict(list)

        for s in strs: 
            sortedS = "".join(sorted(s)) # O(nlogn)
            res[sortedS].append(s)
        
        return list(res.values())



        