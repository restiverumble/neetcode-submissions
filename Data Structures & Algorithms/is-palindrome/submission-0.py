class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        for x in range(len(s)//2):
            if s[x] != s[len(s)-1 - x]:
                return False

        return True