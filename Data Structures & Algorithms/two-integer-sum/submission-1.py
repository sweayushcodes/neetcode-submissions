class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        char_map = {}

        for index, num in enumerate(nums): 
            diff = target - num

            if diff in char_map: 
                return [char_map.get(diff), index]

            char_map[num] = index
        
        return [-1, -1]
        