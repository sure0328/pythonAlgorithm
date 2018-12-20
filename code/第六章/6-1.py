class Solution():
    def solvePermutation(self,array):			
        self.helper(array,[])				#调用helper方法启动
    def helper(self,array,solution):
        if len(array)==0:				#如果没有剩余排序对象
            print(solution)					#输出结果
            return						#返回上一次被调用的地方
        for i in range(len(array)):					#第一本书的选择
            newSolution = solution+[array[i]]		#加入书本
            newArray = array[:i]+array[i+1:]			#删除书本
            self.helper(newArray,newSolution)		#寻找剩余对象的排序集合