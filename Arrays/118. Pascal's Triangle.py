"""118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Input: numRows = 1
Output: [[1]]
-------------------------------------------------------------------------------------
p21 = p10+p11
p31 = p20+p21 p32 = p21+p22
"""
class Solution():
    def pascal(self, numRows):
        pas = [[1]*i for i in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
        return pas


sol = Solution()
ans = sol.pascal(1)
print(ans)                                      #[[1]]

ans = sol.pascal(5)
print(ans)                                      #[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
