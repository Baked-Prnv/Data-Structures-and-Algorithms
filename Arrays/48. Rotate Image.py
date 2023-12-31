"""48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Input: matrix = [[1,2,3],           Output: [[7,4,1],
                 [4,5,6],                    [8,5,2],
                 [7,8,9]]                    [9,6,3]]
Input: matrix = [[5,1,9,11],        Output: [[15,13,2,5],
                 [2,4,8,10],                 [14,3,4,1],
                 [13,3,6,7],                 [12,6,8,9],
                [15,14,12,16]]               [16,7,10,11]]"""


class Solution():
    def rotate(self, matrix):
        left, right  = 0, len(matrix)-1

        while left<right:
            for i in range(right-left):
                top,bottom = left,right

                topLeft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = topLeft

            left+=1
            right-=1

        return matrix
    

print(Solution().rotate(matrix = [[1,2,3],              #[[7, 4, 1],
                                  [4,5,6],              # [8, 5, 2], 
                                  [7,8,9]]))            # [9, 6, 3]]                                                    

print(Solution().rotate(matrix = [[5,1,9,11],           #[[15, 13, 2, 5], 
                                  [2,4,8,10],           # [14, 3, 4, 1],
                                  [13,3,6,7],           # [12, 6, 8, 9], 
                                  [15,14,12,16]]))      # [16, 7, 10, 11]]