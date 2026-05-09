class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        return s == ""




