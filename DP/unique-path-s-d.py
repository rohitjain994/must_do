class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        # for i in range(0,n):
        #     dp[0][i] = 1
        # for i in range(0,m):
        #     dp[i][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j==0:
                    dp[i][j] = 1 
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

# with obstacles

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0: return 0
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,n):
            obstacleGrid[0][i] = int(obstacleGrid[0][i]==0 and obstacleGrid[0][i-1]==1)
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0]==0 and obstacleGrid[i-1][0]==1)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] ==0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return obstacleGrid[m-1][n-1]