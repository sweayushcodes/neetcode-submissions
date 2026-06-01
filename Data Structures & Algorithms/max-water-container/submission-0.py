class Solution:
    def maxArea(self, nums: List[int]) -> int:
        max_vol = 0

        l , r = 0, len(nums) - 1

        while l < r: 
            # smaller one becomes the height
            height = min(nums[l], nums[r])

            # (r - l) becomes width
            width  = r - l

            # volume assignment
            max_vol = max(max_vol, (height * width))

            # move the smaller one
            if nums[l] < nums[r]: 
                l += 1
            else: 
                r -= 1

        return max_vol