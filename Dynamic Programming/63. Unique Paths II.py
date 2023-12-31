"""63. Unique Paths II
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1"""


class Solution():
    def uniquePaths(self, obs_grid):
        rows, cols = len(obs_grid), len(obs_grid[0])
        dp = [0]*cols
        dp[cols-1]=1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obs_grid[r][c]:
                    dp[c]=0
                elif c<cols-1:
                    dp[c] = dp[c] + dp[c+1]

        return dp[0]


print(Solution().uniquePaths(obs_grid = [[0,0,0],       #2
                                         [0,1,0],
                                         [0,0,0]]))     

print(Solution().uniquePaths(obs_grid = [[0,1],         #1
                                         [0,0]]))       