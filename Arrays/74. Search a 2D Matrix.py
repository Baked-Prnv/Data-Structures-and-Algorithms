"""74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false"""

class Solution():
    def search(self, matrix,target):
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1
        while top<=bot:                             #Binary search to find the row
            row = (top+bot)//2
            if target>matrix[row][-1]:
                top = row+1
            elif target<matrix[row][0]:
                bot = row-1
            else:
                break
        
        if not top<=bot:                           #edge case if there isn't any row having target and top>bot(False)
            return False
        
        row = (top+bot)//2                         #row which breaks out of loop
        l,r = 0,COLS-1
        while l<=r:                                #Binary search to find the element from that row
            m = (l+r)//2
            if target>matrix[row][m]:
                l = m+1
            elif target<matrix[row][m]:
                r = m-1
            else:
                return True
        return False
    
sol = Solution()
ans = sol.search(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
print(ans)

ans = sol.search(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
print(ans)