class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        values = set()
        for n in nums:
            if n in values:
                return n
            values.add(n)
        