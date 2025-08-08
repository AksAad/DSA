class Solution:
    def soupServings(self, n: int) -> float:
        n_scaled = ceil(n/25)
        if n_scaled >= 200:
            return 1.0
        memo = {}
        def prob(a: int,b: int) -> float:
            if (a, b) in memo:
                return memo[(a, b)]
            if (a <= 0 and b <= 0):
                return 0.5
            elif(a <= 0 and b > 0):
                return 1.0
            elif(a>0 and b<= 0):
                return 0.0
            result = 0.25 * (prob(a - 4, b) +prob(a - 3, b - 1) +prob(a - 2, b - 2) +prob(a - 1, b - 3))
            memo[(a, b)] = result
            return result
        return prob(n_scaled, n_scaled)


        