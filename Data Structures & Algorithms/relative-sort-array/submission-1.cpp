class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> arr2_set(arr2.begin(), arr2.end());
        unordered_map<int, int> arr1_count;
        vector<int> end;
        for(int n : arr1){
            if(arr2_set.find(n) == arr2_set.end()) end.push_back(n);
            arr1_count[n]++;
        }
        sort(end.begin(), end.end());
        vector<int> res;
        for(int n : arr2){
            for(int i=0; i<arr1_count[n]; i++){
                res.push_back(n);
            }
        }
        res.insert(res.end(), end.begin(), end.end());
        return res;
    }
};