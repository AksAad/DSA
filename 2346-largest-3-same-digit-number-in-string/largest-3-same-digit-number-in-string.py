class Solution:
    def largestGoodInteger(self, num: str) -> str:
        compare = []
        i = 0
        flag = 0
        while i + 3 <= len(num):
            if num[i] == num[i+1] == num[i+2]:
                compare.append(num[i:i+3])
                flag += 1
            i+=1
        compare.sort()
        if flag > 0:
            return compare[-1]
        else:
            return ""
        