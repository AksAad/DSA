class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        minBox = 0
        totalApple = sum(apple)
        for i in range(0,len(capacity)):
            if totalApple <= 0:
                break
            totalApple = totalApple - capacity[i]
            minBox += 1
        return minBox