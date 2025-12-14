class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        total_s = corridor.count('S')
        if total_s == 0 or total_s % 2 != 0:
            return 0
        ways = 1
        s_seen = 0
        p_count = 0 
        for ch in corridor:
            if ch == 'S':
                s_seen += 1
                if s_seen % 2 == 0:
                    ways = (ways * (p_count + 1)) % MOD
                    p_count = 0
            else:
                if s_seen >= 2 and s_seen % 2 == 0:
                    p_count += 1
        return ways
