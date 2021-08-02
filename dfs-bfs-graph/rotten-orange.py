class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))
        time = 0
        while len(queue)>0:
            x,y,t = queue.pop(0)
            for i,j in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0<=i<m and 0<=j<n and grid[i][j]==1:
                    grid[i][j]=2
                    queue.append((i,j,t+1))
                    time = t+1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return time