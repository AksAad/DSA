class Solution:
    def totalMoney(self, n: int) -> int:
        i = 0
        total = 0
        for i in range(1,n//7 +1):
            total += (7/2) * ((2*i) +(6))
        j = (n%7)
        total += (j/2) * ((2*(i+1)) + (j-1))
        return int(total)     
