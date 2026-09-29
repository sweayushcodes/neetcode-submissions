class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # list is not sorted
        # sorting introduces TC of O(nlogN)
        # need another approach
        count = {}

        for i, num in enumerate(nums): 
            if target - num in count: 
                return [count[target-num], i]
            count[num] = i 
        
        return [-1, -1]