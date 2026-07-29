class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        def binary_search(low, high):
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid
            return -1

        result = binary_search(0, l - 1)
        if result != -1:
            return result

        return binary_search(l, len(nums) - 1)