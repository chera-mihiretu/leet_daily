class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        int last = n * n;
        
        bool p = true;
        map<int, pair<int,int>> mp;
        int label = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (p) {
                for (int j = 0; j < n; j++) {
                    mp[label++] = make_pair(i, j);
                }
            } else {
                for (int j = n - 1; j >= 0; j--) {
                    mp[label++] = make_pair(i, j);
                }
            }
            p = !p;
        }

        queue<pair<int,int>> q;
        vector<bool> visited(last + 1, false);

        q.push(make_pair(1, 0));
        visited[1] = true;

        while (!q.empty()) {
            auto [val, count] = q.front();
            q.pop();

            if (val == last) {
                return count;
            }

            for (int nxt = val + 1; nxt <= min(val + 6, last); nxt++) {
                auto [r, c] = mp[nxt];
                int finalSquare = (board[r][c] == -1 ? nxt : board[r][c]);

                if (!visited[finalSquare]) {
                    visited[finalSquare] = true;
                    q.push(make_pair(finalSquare, count + 1));
                }
            }
        }

        return -1;
    }
};