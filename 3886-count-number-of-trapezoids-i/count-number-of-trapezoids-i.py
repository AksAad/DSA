class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        points.sort(key=lambda e: e[1])
        grouped = {k: list(v) for k, v in groupby(points, key=lambda e: e[1])}
        choices = []
        for y, pts in grouped.items():
            c = len(pts)
            if c >= 2:
                choices.append(c * (c - 1) // 2)
        if len(choices) < 2:
            return 0
        S = sum(choices)
        squareSum = sum(x * x for x in choices)
        ans = (S * S - squareSum) // 2
        return ans % (10 ** 9 + 7)
