class Solution {
public:
    long long distributeCandies(int n, int limit) {
        long long answer = 0;

        for (int i = 0; i <= min(limit, n); ++i) {
            int temp = n;
            temp -= i;

            if (temp > (limit * 2)) continue;

            int left = max(0, temp - limit);
            int right = temp - left;

            answer += abs(left - right) + 1;
        }

        return answer;

    }
};