class Solution {
    vector<string> cols;
    void getCols(int p, int m, string s) {
        if (m == 0) {
            cols.push_back(s);
            return;
        }
        for (int i = 0; i < 3; i++) {
            char a = (i + '0');
            if (i != p)
                getCols(i, m - 1, s + a);
        }
    }
    bool isEdge(string& a, string& b) {
        for (int i = 0; i < a.size(); i++)
            if (a[i] == b[i])
                return false;
        return true;
    }
#define ll long long
    ll dp[48][1001];
    int mod = 1000000007;
    ll dfs(int u, int n, vector<vector<int>>& G) {
        if (n == 0)
            return 1LL;
        if (dp[u][n] != -1)
            return dp[u][n];
        ll res = 0;
        for (auto& v : G[u])
            res = (res + dfs(v, n - 1, G)) % mod;
        return dp[u][n] = res;
    }

public:
    int colorTheGrid(int m, int n) {
        getCols(-1, m, "");
        int nodes = cols.size();
        vector<vector<int>> G(nodes);
        for (int i = 0; i < nodes; i++) {
            for (int j = i + 1; j < nodes; j++) {
                if (isEdge(cols[i], cols[j])) {
                    G[i].push_back(j);
                    G[j].push_back(i);
                }
            }
        }
        memset(dp, -1, sizeof(dp));
        ll res = 0;
        for (int i = 0; i < nodes; i++)
            res = (res + dfs(i, n - 1, G)) % mod;
        return res;
    }
};