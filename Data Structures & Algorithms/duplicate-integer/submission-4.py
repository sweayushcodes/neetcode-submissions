class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # list can be empty
        # couple of ways of solving this problem
        # 1. set -> add all elements and then return when you find an existing element in the set
        # 2. frequency map {num : count} - overkill 
        # 3. AI optimised - len(Counter(nums)) == len(nums)
        # 4. sort and compare adjancent elements 

        seen = set()

        for num in nums: 
            if num in seen: 
                return True
            seen.add(num)
        
        return False


        