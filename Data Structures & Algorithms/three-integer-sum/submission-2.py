class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip everything below => i++ since i is duplicate
            l, r, s = i+1, len(nums) - 1, 0 - nums[i] # implement 2 Sum
            while l < r:
                if nums[l] + nums[r] < s:
                    l += 1
                elif nums[l] + nums[r] > s:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: # if l duplicate
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # if r duplicate
                        r -= 1
                    l += 1
                    r -= 1
        return res