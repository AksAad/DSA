class Solution:
    def sortVowels(self, s: str) -> str:
        check = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = []
        indices_at = []
        for i in range(0,len(s)):
            if s[i] in check:
                vowels.append(s[i])
                indices_at.append(i)
        t = []
        indices_at = set(indices_at)
        vowels = sorted(vowels)
        j = 0
        for i in range(0,len(s)):
            if i in indices_at :
                t.append(vowels[j])
                j+=1
            else:
                t.append(s[i])                
        return "".join(t)
