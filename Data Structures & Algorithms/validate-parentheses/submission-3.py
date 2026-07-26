class Solution:
    charMap = {
        "(" : ")",
        "{" : "}",
        "[" : "]",
    }

    def isValid(self, s: str) -> bool:
        if (len(s) % 2 == 1):
            return False
        
        stack = []
        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if self.charMap[check] != char:
                    return False
        return len(stack) == 0