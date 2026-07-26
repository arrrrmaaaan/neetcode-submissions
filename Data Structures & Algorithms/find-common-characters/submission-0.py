class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])

        for i in range(1, len(words)):
            w = words[i]
            currFreq = Counter(w)
            for j in freq:
                freq[j] = min(freq[j], currFreq[j])

        res = []
        for j in freq:
            for i in range(freq[j]):
                res.append(j)

        return res