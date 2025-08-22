class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        i = 0
        flag = 0
        area = []
        curr_col = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and flag == 0:
                    area.append(i)
                    area.append(j)
                    curr_col = j
                    flag += 1  
                elif curr_col > j and grid[i][j] == 1:
                    del area[-1]
                    area.append(j)
                    curr_col = j
        flag = 0
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and flag == 0:
                    area.append(i)           
                    curr_col = j
                    area.append(j)
                    flag += 1
                elif curr_col < j and grid[i][j] == 1:
                    del area[-1]
                    curr_col = j
                    area.append(curr_col)
        height = area[2] - area[0] + 1       
        breadth = area[3] - area[1] + 1     
        return height * breadth
