"""289. Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. 
Given the current state of the m x n grid board, return the next state.
Input: board = [[0,1,0],                    Output: [[0,0,0],
                [0,0,1],                             [1,0,1],
                [1,1,1],                             [0,1,1],
                [0,0,0]]                             [0,1,0]]
Input: board = [[1,1],                      Output: [[1,1],
                [1,0]]                               [1,1]]
--------------------------------------------------------------------
ORIGINAL | NEW | STATE
    0    |  0  |  0
    1    |  0  |  1
    0    |  1  |  2
    1    |  1  |  3"""


class Solution():
    def gameOfLife(self,board):
        ROWS, COLS = len(board),len(board[0])

        def countNeighbour(r,c):
            nei = 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if (i<0 or                          #if row goes out og bound (-1)th
                        j<0 or                          #if col goes out if bound (-1)th
                        i==ROWS or                      #if row goes out of bound (ROW+1)th
                        j==COLS or                      #if col goes out if bound (COL+1)th
                        (i==r and j==c)):               #not considering (r,c) for counting 
                        continue
                    if board[i][j] in [1,3]:            #if STATE value is 1,3 ie., ORIGINAL_value was 1
                        nei += 1                        
            return nei

        for r in range(ROWS):
            for c in range(COLS):
                nei = countNeighbour(r,c)
                if board[r][c]:                         #if there is a live cell
                    if nei in [2,3]:                        #if neig are 2,3, it lives
                        board[r][c] = 3                     #mark STATE 3 with NEW_value 1
                elif nei == 3:                          #if dead cell and neig are =3, it lives   
                        board[r][c] = 2                     #mark STATE 2 with NEW_value 1

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:                    #if State is 1, NEW_value is 0
                    board[r][c] = 0
                elif board[r][c] in [2,3]:              #if state is2,3, NEW_value is 1
                    board[r][c] = 1


board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]
Solution().gameOfLife(board)
print(board)                                            #[[0, 0, 0], 
                                                        # [1, 0, 1], 
                                                        # [0, 1, 1], 
                                                        # [0, 1, 0]]

board = [[1,1],
         [1,0]]
Solution().gameOfLife(board)
print(board)                                            #[[1, 1], 
                                                        # [1, 1]]                                                   