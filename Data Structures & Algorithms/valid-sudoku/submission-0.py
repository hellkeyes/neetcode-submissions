class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = False
        cols = False
        box = False
        for i in range(len(board)):
            myset = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                else:
                    if 9 >= int(board[i][j]) >= 1:
                        if board[i][j] in myset:
                            return False
                        myset.add(board[i][j])
        rows = True

        for i in range(len(board)):
            myset = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                else:
                    if 9 >= int(board[j][i]) >= 1:
                        if board[j][i] in myset:
                            return False
                        myset.add(board[j][i])
        cols = True

        mylist = [[0, 3, 0, 3],
            [0, 3, 3, 6],
            [0, 3, 6, 9],
            [3, 6, 0, 3],
            [3, 6, 3, 6],
            [3, 6, 6, 9],
            [6, 9, 6, 9],
            [6, 9, 6, 9],
            [6, 9, 6, 9]]
    
        for i in range(len(mylist)):
            myset = set()
            for x in range(mylist[i][0], mylist[i][1]):
                for y in range(mylist[i][2], mylist[i][3]):
                    if board[x][y] == '.':
                        continue
                    else:
                        if 9 >= int(board[x][y]) >= 1:
                            if board[x][y] in myset:
                                return False
                            myset.add(board[x][y])

        box = True
     
        if cols == True and box == True and rows == True:
            return True
