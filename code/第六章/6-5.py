class Solution():
    def solveSudoku(self, board):
        self.helper(board, 0)
    def helper(self, board, index):
        if index >= 81:			#如果盘面已满
            self.printSolution(board)		#输出结果
            return					#返回上一格
        if board[index] == 0:			#如果当前格为空格
            for i in range(1, 10):		#依次假设1-9
                if self.isValid(board, index, i): #如果假设成立
                    board[index] = i		#填入数字
                    self.helper(board, index + 1)	#继续假设
                    board[index] = 0
        else:						#如果当前格有已知数
            self.helper(board,index+1)		#跳过此格
    def printSolution(self, board): 			#输出结果
        for i in range(0,81,9):	
            print(board[i:i+9])

    def isValid(self, board, index, num):	  #isValid方法检查当前假设是否合理
        row = index // 9				#当前格子的行数
        column = index % 9				#当前格子的列数
        for i in range(index + 9, 81, 9):	  #检查和同列（下方）的格子是否矛盾
            if board[i] == num:
                return False
        for i in range(index - 9, -1, -9):#检查和同列（上方）的格子是否矛盾
            if board[i] == num:
                return False
        for i in range(9 * row, 9 * (row + 1)):	#检查和同行的格子是否矛盾
            if board[i] == num:
                return False
        for i in range(row - row % 3, 3 + row - row % 3):  #检查和同粗线格的格子是否矛盾
            for j in range(column - column % 3, 3 + column - column % 3):
                if board[j + i * 9] == num:
                    return False
        return True