class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        i = len(energy) - 1
        dp = [0] * len(energy)
        while i >= 0:
            if i + k < len(energy):
                dp[i] = energy[i] + dp[i+k]
            else:
                dp[i] = energy[i]
            i-=1
        return max(dp)