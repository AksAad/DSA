class Solution:
    def bestClosingTime(self, customers: str) -> int:
        maxScore, totalScore, time = 0, 0, 0
        for i, ch in enumerate(customers, start = 1):    
            totalScore += 1 if ch == 'Y' else -1  
            if maxScore < totalScore:
                maxScore = totalScore
                time = i
            else:
                continue
        return time