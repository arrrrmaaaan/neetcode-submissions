class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        i = 0
        j = n - 1
        while i <= j:
            front = s[i].lower()
            back = s[j].lower()

            if not front.isalnum() or front == ' ':
                i += 1
                continue
            if not back.isalnum() or back == ' ':
                j -= 1
                continue

            if front != back:
                return False
            
            i += 1
            j -= 1
        return True