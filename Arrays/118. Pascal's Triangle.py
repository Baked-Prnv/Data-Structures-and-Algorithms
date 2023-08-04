"""118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Input: numRows = 1          Output: [[1]]
Input: numRows = 5          Output: [[1],
                                    [1,1],
                                   [1,2,1],
                                  [1,3,3,1],
                                 [1,4,6,4,1]]
-------------------------------------------------------------------------------------
p21 = p10+p11
p31 = p20+p21 and p32 = p21+p22
pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
"""
class Solution():
    def pascal(self, numRows):
        pas = [[1]*i for i in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
        return pas


print(Solution().pascal(1))          #[[1]]

print(Solution().pascal(5))         #[[1], 
                                   #[1, 1], 
                                  #[1, 2, 1], 
                                #[1, 3, 3, 1], 
                               #[1, 4, 6, 4, 1]]
