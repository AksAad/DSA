class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        return (n & (n-1)) == 0 and (n-1) % 3 == 0
        