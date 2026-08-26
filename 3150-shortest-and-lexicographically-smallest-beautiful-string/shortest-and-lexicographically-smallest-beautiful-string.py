class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        cnt = 0
        min_len = float('inf')
        ans = ""
        for r in range(len(s)):
            if s[r] == '1':
                cnt += 1
            while cnt == k:
                curr = s[l:r + 1]

                if min_len > r - l + 1:
                    min_len = r - l + 1
                    ans = curr
                elif min_len == r - l + 1:
                    if ans > curr:
                        ans = curr
                if s[l] == '1':
                    cnt -= 1
                l += 1
        return ans