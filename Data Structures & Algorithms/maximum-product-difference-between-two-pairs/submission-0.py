class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        start = nums[0] * nums[1]
        end = nums[n-1] * nums[n-2]
        return end - start