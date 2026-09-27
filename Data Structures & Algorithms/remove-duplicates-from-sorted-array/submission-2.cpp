class Solution {
   public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int l = 1, r = 1, res = 1;
        while (r < n) {
            if (nums[r] == nums[r - 1]) {
                r++;
                continue;
            }
            nums[l++] = nums[r++];
        }
        return l;
    }
};