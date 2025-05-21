class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> row_col[2];

        for (int i = 0; i < matrix.size(); ++ i ) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == 0) {
                    row_col[0].insert(i);
                    row_col[1].insert(j);
                }
            }
        }

        for (int i = 0; i < matrix.size(); ++ i ) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (row_col[0].find(i) != row_col[0].end() || row_col[1].find(j) != row_col[1].end()){
                    matrix[i][j] = 0;
                }
            }
        }



    }
};