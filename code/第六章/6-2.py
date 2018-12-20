class Solution(): 
   def solveCombination(self,array,n):
       self.helper(array,n,[])				#调用helper方法起始
   def helper(self,array,n,solution):			#helper方法
       if len(solution) == n:					#如果solution中有n门课程
           print (solution)					#输出结果
           return							#返回被调用的地方
       for i in range(len(array)):					#for每一个课目选项
           newSolution = solution + [array[i]]			#把课程加入到新的组合列表
           newArray = array[i + 1:]					#创建新课程列表，更新列表
           self.helper(newArray,n,newSolution)			#调用helper方法选择剩余课程