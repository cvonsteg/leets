class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> vals;
        vector<int> result;
        for(int i = 0; i < nums.size(); i++) {
            if (vals.count(target - nums[i])) {
                result.push_back(vals[target - nums[i]]);
                result.push_back(i);
            }
            vals[nums[i]] = i;
        }
        return result;
    }
};
