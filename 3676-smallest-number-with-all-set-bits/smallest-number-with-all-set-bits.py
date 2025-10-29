class Solution:
    def smallestNumber(self, n: int) -> int:
        binary_num = bin(n)[2:]
        return int(str(binary_num).replace('0','1'),2)