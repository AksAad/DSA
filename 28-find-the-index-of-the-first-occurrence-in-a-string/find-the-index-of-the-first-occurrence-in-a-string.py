class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if  len(haystack) < len(needle):
            return -1
        i = 0
        k = len(needle)
        for i in range(len(haystack) - k + 1):
            if haystack[i:i+k] == needle:
                return i
        return -1