class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>,vector<string>> mp;
        for(auto s : strs){
            vector<int> freq(26,0);
            for(auto c : s){
                freq[c - 'a']++;
            }
            mp[freq].push_back(s);
        }
        vector<vector<string>> res;
        for(auto [key, value] : mp){
            res.push_back(value);
        }
        return res;
    }
};
