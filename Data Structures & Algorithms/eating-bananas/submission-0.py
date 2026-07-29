class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minSpeed = right

        while left <= right:
            mid = left + ((right - left) // 2)
            totalTime = 0

            for b in piles:
                totalTime += math.ceil(b / mid)

            if totalTime <= h:
                minSpeed = mid
                right = mid - 1
            else:
                left = mid + 1
        return minSpeed