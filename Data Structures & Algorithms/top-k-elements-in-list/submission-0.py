class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        heap = []
        for key in freq:
            heapq.heappush(heap, (freq[key], key))
            if (len(heap) > k):
                heapq.heappop(heap)

        res = []
        for val in heap:
            res.append(val[1])
        return res