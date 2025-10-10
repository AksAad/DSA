class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        have = 0
        t_count = Counter(t)
        window_count = {}
        left = 0
        need = len(t_count)
        min_length = None
        min_start = None
        for right,char in enumerate(s):
            window_count[char] = window_count.get(char,0) + 1
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            while have == need:
                current_length = right - left + 1
                if min_length is None or current_length < min_length:
                    min_length = current_length
                    min_start = left
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        if min_start is None:
            return "" 
        return s[min_start:min_start + min_length]