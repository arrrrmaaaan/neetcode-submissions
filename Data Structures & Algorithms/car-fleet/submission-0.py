class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        group = [(pos, spd) for pos, spd in zip(position, speed)]
        group.sort(reverse=True)

        stack = []
        for pos, spd in group:
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)