class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        const int MOD = 1e9 + 7;
        vector<long long> dp(n + 1, 0);
        dp[1] = 1;

        for (int day = 1; day <= n; day++) {
            long long people_today = dp[day];
            if (people_today == 0) continue;


            int start = day + delay;
            int end = day + forget;

            for (int next_day = start; next_day < end && next_day <= n; next_day++) {
                dp[next_day] = (dp[next_day] + people_today) % MOD;
            }
        }
        long long result = 0;
        for (int day = n - forget + 1; day <= n; day++) {
            if (day > 0) {
                result = (result + dp[day]) % MOD;
            }
        }

        return (int)result;
    }
};
