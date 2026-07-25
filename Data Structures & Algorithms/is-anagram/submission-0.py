class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False

        seen = defaultdict(int)
        for letter in s:
            seen[letter] += 1

        for letter in t:
            seen[letter] -= 1

            if seen[letter] == 0:
                del seen[letter]

        if seen == {}:
            return True
        return False