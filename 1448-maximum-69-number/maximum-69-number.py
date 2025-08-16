class Solution:
    def maximum69Number (self, num: int) -> int:
        digit = [int(digit) for digit in str(num)]
        for i in range(0,len(digit)):
            if digit[i] != 9:
                digit[i] = 9
                break
            else:
                continue
        return int(''.join(map(str,digit)))