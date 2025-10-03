class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m-1 or c == 0 or c == n-1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        total_water = 0
        while heap:
            height, r, c = heapq.heappop(heap)
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    trapped = max(0, height - heightMap[nr][nc])
                    total_water += trapped
                    new_height = max(heightMap[nr][nc], height)
                    heapq.heappush(heap, (new_height, nr, nc))
        return total_water