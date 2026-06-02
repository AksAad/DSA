class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        currmin = 0
        cost.sort(reverse = True)
        total = 0
        for i in range(0,len(cost)):
            if (i+1) % 3 == 0:
                continue
            else:
                total+=cost[i]

        return total