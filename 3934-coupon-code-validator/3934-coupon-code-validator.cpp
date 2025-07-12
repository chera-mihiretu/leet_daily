class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        vector<pair<string, string>> answer;
        unordered_set<string> validBL = {"electronics", "grocery", "pharmacy", "restaurant"};
        for (int i = 0; i < code.size(); i ++ ) {
            if (isActive[i]) {
                if (validBL.find(businessLine[i] )!= validBL.end()) {
                    bool valid = true;

                    for (int j = 0 ; j < code[i].length(); j ++ ) {
                        if (('a' <=  code[i][j] && code[i][j] <= 'z') || ('A' <= code[i][j] && code[i][j] <= 'Z') || ('0' <= code[i][j] && code[i][j] <= '9') || (code[i][j] == '_')) continue;
                        valid = false;
                        break;
                    }
                    if (valid && code[i] != "") answer.push_back({businessLine[i], code[i]});
                }
            }
        }
        sort(answer.begin(), answer.end());

        vector<string> last_answer;

        for (auto [f, s] : answer) {
            last_answer.push_back(s);
        }

        return last_answer;
    }
};