class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            int indexFound = m[target - nums[i]];
            if (indexFound != 0) {
                return {indexFound - 1, i};
            }
            m[nums[i]] = i + 1;
        }
        return {};
    }
};
