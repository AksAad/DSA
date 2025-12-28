class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(0,len(grid)):
            count += sum(1 for num in grid[i] if num < 0)
        return count