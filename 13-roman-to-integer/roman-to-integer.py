class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = {"I" : 1 , "V" : 5 , "X" : 10 , "L" : 50, "C" : 100, "D": 500, "M" : 1000}
        i = 0
        total = 0
        while i < len(s):
            current = value[s[i]]
            if (i+1) < len(s) and value[s[i]] < value[s[i + 1]]:
                total += value[s[i + 1]] - value[s[i]]
                i += 2
            else:
                total += current
                i += 1
        return total
