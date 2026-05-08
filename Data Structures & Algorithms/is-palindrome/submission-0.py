class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for w in s:
            if w.isalnum():
                p += w.lower()
        for i in range(len(p)):
            if p[i] != p[len(p)-i-1]:
                return False
        return True