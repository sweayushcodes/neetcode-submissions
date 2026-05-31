class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0 

        elements  = defaultdict(bool)

        for num in nums: 
            elements[num] = False

        for num in nums: 
            count = 1

            while num + 1 in elements and elements[num] == False: 
                count += 1
                num += 1

            result = max(result, count)
        
        return result
            

        