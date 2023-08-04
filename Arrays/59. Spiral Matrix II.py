"""59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Input: n = 3                Output: [[1,2,3],
                                     [8,9,4],
                                     [7,6,5]]
Input: n = 1                Output: [[1]]"""

class Solution():
    def spiral(self, n):
        res = [[0]*n for _ in range(n)]
        left,right = 0,n
        top,bottom = 0,n
        val = 1

        while left<right and top<bottom:
            for c in range(left,right):
                res[top][c] = val
                val+=1
            top+=1
            for r in range(top,bottom):
                res[r][right-1]=val
                val+=1
            right-=1
            for c in range(right-1,left-1,-1):
                res[bottom-1][c] = val
                val+=1
            bottom-=1
            for r in range(bottom-1,top-1,-1):
                res[r][left] = val
                val+=1
            left+=1
            
        return res
    

print(Solution().spiral(1))                     #[[1]]

print(Solution().spiral(3))                     #[[1, 2, 3], 
                                                # [8, 9, 4], 
                                                # [7, 6, 5]]

print(Solution().spiral(4))                     # [[1, 2, 3, 4], 
                                                #[12, 13, 14, 5], 
                                                #[11, 16, 15, 6], 
                                                # [10, 9, 8, 7]]

print(Solution().spiral(5))                     #  [[1, 2, 3, 4, 5], 
                                                # [16, 17, 18, 19, 6], 
                                                # [15, 24, 25, 20, 7], 
                                                # [14, 23, 22, 21, 8], 
                                                # [13, 12, 11, 10, 9]]