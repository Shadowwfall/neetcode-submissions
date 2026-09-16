class Solution {
   public:
    bool isValid(string s) {
        stack<int> stack;
        unordered_map<char, char> mp = {{')', '('}, {']', '['}, {'}', '{'}};
        for (char b : s) {
            if (mp.find(b) != mp.end()) {
                if (!stack.empty() && stack.top() == mp[b]) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(b);
            }
        }
        return stack.empty();
    }
};
