class Solution:
    def minPartitions(self, n: str) -> int:
        digits_list = list(map(int, str(n)))
        return max(digits_list)