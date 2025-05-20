class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> preef(nums.size() + 1, 0);
        for (auto& q : queries) {
            int L = q[0] , R = q[1];
            preef[L] ++;
            preef[R + 1] --;
        }
        int p = 0;

        for (int i = 0; i < nums.size(); ++i) {
            p += preef[i];

            if (p < nums[i]) return false;
        }
        return true;
    }
};