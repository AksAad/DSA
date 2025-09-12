class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        s = s.lower()

        if any(ch in vowels for ch in s):
            return True   
        else:
            return False
