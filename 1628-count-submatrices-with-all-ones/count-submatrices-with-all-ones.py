class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        nums = [[0] * m for _ in range(n)]
        for i in range(n):
            if mat[i][m-1] == 1:
                nums[i][m-1] = 1
            else:
                nums[i][m-1] = 0
            for j in range(m-2, -1, -1):
                nums[i][j] = 0 if mat[i][j] == 0 else nums[i][j+1] + 1
        
        submat = 0
        for i in range(n):
            for j in range(m):
                width = nums[i][j]
                for d in range(i, n):
                    if nums[d][j] == 0:
                        break
                    width = min(width, nums[d][j])
                    submat += width
        return submat
