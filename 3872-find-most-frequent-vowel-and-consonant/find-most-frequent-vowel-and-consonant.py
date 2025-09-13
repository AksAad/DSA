class Solution:
    def maxFreqSum(self, s: str) -> int:
        s = s.lower()
        check = Counter(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowel = 0
        max_consonant = 0
        for char, freq in check.items():
            if char in vowels:
                max_vowel = max(max_vowel, freq)
            else:
                max_consonant = max(max_consonant, freq)
        return max_vowel + max_consonant
