class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Big O: Sorting is n log n
        nums.sort()
        ret = set()

        # Big O: For loop is n
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1

            # Big O: Nested For loop, worst case n-1 times so O(n) * O(n-1) = O(n**2)
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    # ret.append([nums[i], nums[j], nums[k]])
                    arr = [nums[i], nums[j], nums[k]]
                    ret.add(tuple(arr))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1

        ret = [list(triplet) for triplet in ret]
        return ret