class Solution:
    def encode(self, strs: List[str]) -> str:
        retStr = ''
        for s in strs:
            n = len(s)
            retStr += str(n)
            retStr += ':'
            retStr += s
        return retStr

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []

        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            size = int(s[i:j])
            i = j + 1

            word = s[i:i+size]
            ret.append(word)
            i += size

        return ret