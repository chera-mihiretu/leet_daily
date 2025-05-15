class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        vector<string> answer;

        answer.push_back(words[0]);
        int index = 0;

        for (int i =1; i < words.size(); ++i) {
            if (groups[index] != groups[i]) {
                answer.push_back(words[i]);
                index = i;
            }
        }

        return answer;
    }
};