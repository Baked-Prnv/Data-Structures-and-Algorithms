"""54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Input: matrix = [[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]"""

class Solution():
    def spiral(self, matrix):
        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left<right and top<bottom:
            for i in range(left,right):                 #gets every i from top row
                res.append(matrix[top][i])
            top+=1
            for i in range(top, bottom):                #gets every i from right col
                res.append(matrix[i][right-1])
            right-=1
            
            if not (left<right and top<bottom):         #edge case if the matrix is a col or row matrix
                break
            
            for i in range(right-1,left-1,-1):          #gets every i from bottom row
                res.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):          #gets every i from left col
                res.append(matrix[i][left])
            left+=1
        return res

sol = Solution()
ans = sol.spiral(matrix = [[1,2,3],
                           [4,5,6],
                           [7,8,9]])
print(ans)                              #[1, 2, 3, 6, 9, 8, 7, 4, 5]

ans = sol.spiral(matrix = [[1,2,3,4],
                           [5,6,7,8],
                          [9,10,11,12]])
print(ans)                              #[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]