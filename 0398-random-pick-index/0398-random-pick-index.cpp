class Solution {
    unordered_map<int, pair<vector<int>, int>> mp; // ele -> {indexes, it}
public:
    Solution(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<n;i++){
            if(mp.count(nums[i]) == 0){
                mp[nums[i]].second = 0;
            }
            mp[nums[i]].first.push_back(i);
        }
    }
    
    int pick(int target) {
        vector<int> &a = mp[target].first;
        int sz = a.size();
        int it = mp[target].second;
        
        mp[target].second = (it+1)%sz;
        return a[it];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 ["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]], [[3]]

 3 - 2,3,4
 map ele -> {indexes, iter}
 
 TC:
 Solution: O(N)
 Pick: O(1)
 
 SC: O(M)
 M-> unique
 
 */