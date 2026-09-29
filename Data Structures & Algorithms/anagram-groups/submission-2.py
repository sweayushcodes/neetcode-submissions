class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can you use string as a key in maps?? 
        # is it hashed when stored & used as a key? 
        # 

        res = defaultdict(list)

        for s in strs: 
            key = "".join(sorted(s)) # O(nlogn)
            if key in res: 
                res[key].append(s)
            else: 
                res[key].append(s)
        
        return [value for value in res.values()]



        