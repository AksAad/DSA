class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = []
        for num in bank:
            if num.count("1") == 0:
                pass
            else:
                count.append(num.count("1"))
        total = 0
        for n in range(0,len(count)-1):
            total += count[n] * count[n+1]
        return total
            