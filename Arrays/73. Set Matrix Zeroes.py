"""73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Input: matrix = [[1,1,1],           Output: [[1,0,1],
                 [1,0,1],                    [0,0,0],
                 [1,1,1]]                    [1,0,1]]

Input: matrix = [[0,1,2,0],         Output: [[0,0,0,0],
                 [3,4,5,2],                  [0,4,5,0],
                 [1,3,1,5]]                  [0,3,1,0]]
Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?"""


class Solution():
    def setZeros(self,matrix):
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r>0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for r in range(rows):
                matrix[r][0]=0

        if rowZero:
            for c in range(cols):
                matrix[0][c]=0

        return matrix
    

print(Solution().setZeros(matrix = [[1,1,1],                    #[[1, 0, 1],
                                    [1,0,1],                    # [0, 0, 0],
                                    [1,1,1]]))                  # [1, 0, 1]]
                                                    
print(Solution().setZeros(matrix = [[0,1,2,0],                  #[[0, 0, 0, 0],
                                    [3,4,5,2],                  # [0, 4, 5, 0],
                                    [1,3,1,5]]))                # [0, 3, 1, 0]]