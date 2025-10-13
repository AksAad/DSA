class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 0
        while i in range(0,len(words)-1):
            a1 = Counter(words[i])
            b1 = Counter(words[i+1])
            if a1 == b1:
                words.remove(words[i+1])
            else:
                i+=1
        return words