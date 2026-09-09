class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftMost = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                leftMost = m
                r = m -1
            elif nums[m] > target:
                r = m - 1
            else: l = m + 1
        rightMost = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                rightMost = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else: l = m + 1
        if leftMost == -1:
            return [-1, -1]
        return [leftMost, rightMost]
        
            