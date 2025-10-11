class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        #dmg = power[i] cannot do dmg of power[i] +- 1 and +- 2
        curr_power = power[0]
        p = Counter(power)
        vals = sorted(p.keys())
        dp = [0] * (len(vals) + 1)
        for i,v in enumerate(vals):
            gain = p[v] * v
            j = i - 1
            while j >= 0 and vals[j] >= v - 2:
                j-=1
            take = gain +( dp[j+1] if j >= 0 else 0)
            skip = dp[i]
            dp[i+1] = max(take,skip)
        return max(dp)