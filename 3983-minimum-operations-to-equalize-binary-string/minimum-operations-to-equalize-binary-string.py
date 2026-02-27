class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zero = s.count('0')
        if zero == 0:
            return 0
        one = n - zero
        for ops in range(1, n + 1):
            total_flip = ops * k
            if (total_flip - zero) % 2 != 0:
                continue
            if ops % 2 == 1:
                if zero <= total_flip <= zero * ops + one * (ops - 1):
                    return ops
            else:
                if zero <= total_flip <= zero * (ops - 1) + one * ops:
                    return ops
        return -1