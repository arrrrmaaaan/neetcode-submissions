class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Store as (idx, temp)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                sIdx, sTemp = stack.pop()
                res[sIdx] = idx - sIdx
            stack.append([idx, temp])
        return res