class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = set(list(brokenLetters))
        g = text.split()
        w = 0
        fl = 0
        for i in g:
            for char in i:
                if char in l:
                    fl = 1
                    break
                else:
                    fl = 0
            if fl == 0:
                w += 1
        return w