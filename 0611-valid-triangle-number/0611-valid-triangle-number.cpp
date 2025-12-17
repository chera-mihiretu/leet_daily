class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int answer = 0;
        for (int i = 0; i < nums.size(); i++ ) {
            for (int j = i + 1; j < nums.size(); j ++) {
                int size = lower_bound(nums.begin() + j + 1, nums.end(), nums[i] + nums[j]) - (nums.begin() + j + 1);
                answer += size;
            }
        }
        return answer;
    }
};