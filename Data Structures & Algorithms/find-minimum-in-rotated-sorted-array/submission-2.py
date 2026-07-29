class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 1
        minVal = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break

            mid = l + ((r - l) // 2)
            minVal = min(minVal, nums[mid])
            if nums[mid] > minVal:
                l = mid + 1
            else:
                r = mid - 1
        return minVal