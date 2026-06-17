class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = l + k - 1
        while r < len(nums):
            maxNum = max(nums[l: r + 1])
            res.append(maxNum)
            r += 1
            l += 1
        return res