class Solution {
   public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> s;
        int n = asteroids.size();
        for (int i = 0; i < n; i++) {
            if (asteroids[i] > 0) {
                s.push(asteroids[i]);
            } else {
                while (!s.empty() && (s.top() > 0) && (s.top() + asteroids[i] < 0)) {
                    s.pop();
                }
                if (s.empty() || s.top() < 0) {
                    s.push(asteroids[i]);
                } else if (s.top() + asteroids[i] == 0) {
                    s.pop();
                }
            }
        }
        vector<int> ans(s.size());
        int i = s.size() - 1;
        while (!s.empty()) {
            ans[i] = s.top();
            s.pop();
            i--;
        }
        return ans;
    }
};