class Solution():
    def wordSearch(self, board, word):
        for i in range (len(board)):
               for j in range (len(board[0])):        #遍历盘面
                       if self.helper(board,word,i,j):		#调用helper方法
                           return True
        return False
    def helper(self,board,current,row,column):			#helper方法（回溯方法）
        if len(current)==0:							#结束条件
            return True
        if row>=0 and row<len(board) and column>=0 and column<len(board[0]): #前提条件
            if board[row][column] == current[0]:			#如果两个字母对应
                board[row][column]=""
                if self.helper(board,current[1:],row-1,column):	#上下左右检查剩余字母
                    return True
                if self.helper(board,current[1:],row+1,column):
                    return True
                if self.helper(board,current[1:],row,column-1):
                    return True
                if self.helper(board,current[1:],row,column+1):
                    return True
                board[row][column]=current[0]  
        return False