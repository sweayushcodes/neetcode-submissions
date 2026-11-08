class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for index, num in enumerate(nums): 
            if (target - num) in diff:
                return [diff[target - num], index]
            diff[num] = index
        
        return [-1, -1]

        