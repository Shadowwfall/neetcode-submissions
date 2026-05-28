class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        cur = s[i]
        for l in t:
            print(i)
            print(s[i])
            if l == cur:
                i += 1
                if i == len(s):
                    return True
                cur = s[i]
            if i == len(s):
                print("here!")
                return True
        return False