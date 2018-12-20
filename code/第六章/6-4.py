class Solution(object):
 
     def solveNQueens(self, n):
         self.helper([-1]*n, 0, n)
 
     def helper(self, columnPositions, rowIndex, n):	#helper方法
         if rowIndex == n:								#rowIndex代表当前行
             self.printSolution(columnPositions,n)		#如果走完了所有行就输出结果
             return									#返回到上一行的假设
         for column in range(n):
             columnPositions[rowIndex] = column		#假设第rowIndex行的保安位置
             if self.isValid(columnPositions, rowIndex):			#如果可行
               self.helper(columnPositions, rowIndex+1, n)	#继续假设剩余行的保安位置
               
     def isValid(self, columnPositions, rowIndex):			#isValid方法检查位置是否合理
         for i in range(rowIndex):
             if columnPositions[i] == columnPositions[rowIndex]: 	#检查同列是否有保安
                 return False
             elif abs(columnPositions[i]-columnPositions[rowIndex]) == rowIndex-i:
                 return False							#检查两条斜线上是否有保安
         return True    
                 
     def printSolution(self, columnPositions, n):				#printSolution方法输出结果
         for row in range (n):
           line = ""
           for column in range (n):
             if columnPositions[row] == column:
               line += "Q "
             else:
               line += ". "
           print(line)
         print("\n")        
 
Solution().solveNQueens(8)					#我们调用solveNQueens解决8皇后问题