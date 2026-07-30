class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            char = s[r]
            if char in mp:
                l = max(mp[char] + 1, l)
            mp[char] = r
            res = max(res, r - l + 1)
        return res