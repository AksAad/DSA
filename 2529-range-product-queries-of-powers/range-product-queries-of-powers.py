class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        #whatever number i get the binary representation of it will have all the powers of 2 which add up to it
        powers = []
        for i in range(31):
            if (n >> i) & 1:
                powers.append(1 << i)
        res = []
        for a, b in queries:
            prod = 1
            for i in range(a, b + 1):
                prod = (prod * powers[i]) % MOD
            res.append(prod)
        
        return res

