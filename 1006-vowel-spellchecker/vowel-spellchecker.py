class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordset = set(wordlist)
        case_map = {}
        for word in wordlist:
            lower = word.lower()
            if lower not in case_map:
                case_map[lower] = word
        def devowel(word):
            vowels = "aeiou"
            return "".join('*' if c in vowels else c for c in word.lower())

        vowel_map = {}
        for word in wordlist:
            key = devowel(word)
            if key not in vowel_map:
                vowel_map[key] = word
        result = []
        for q in queries:
            if q in wordset:
                result.append(q)  
            elif q.lower() in case_map:
                result.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:
                result.append(vowel_map[devowel(q)])
            else:
                result.append("") 
        return result