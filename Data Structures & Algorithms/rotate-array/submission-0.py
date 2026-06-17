class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_array(l, r):
            while l < r: 
                nums[l], nums[r] = nums[r], nums[l]

                l += 1
                r -= 1
        
        k %= len(nums)
        reverse_array(0, len(nums) - 1)
        reverse_array(0, k - 1)
        reverse_array(k, len(nums) - 1)
        