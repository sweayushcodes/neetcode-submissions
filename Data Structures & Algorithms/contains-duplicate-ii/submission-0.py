class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0

        for r, num in enumerate(nums): 
            if r > k:
                seen.remove(nums[l])
                l += 1
            
            if nums[r] in seen: 
                return True
            
            seen.add(num)
            
        return False
                


         


        

        