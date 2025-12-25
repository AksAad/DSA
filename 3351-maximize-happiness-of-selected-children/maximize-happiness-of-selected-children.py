class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = 0
        decrement = 0
        for i in range(0,k):
            if happiness[i] - decrement < 0:
                ans+= 0
            else:
                ans+=happiness[i] - decrement
            decrement+=1
            
        return ans