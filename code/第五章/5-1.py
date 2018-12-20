#广度优先遍历
def bfs(numCourses,preList):
	preListCount=[0]*numCourses
	for line in preList:				#取出二维数组的每一行
		for i in range(len(line)):		#针对每一行来为preListCount赋值
			if line[i]==1:
				preListCount[i]+=1
	canTake=[]
	for i in range(len(preListCount)):
		if preListCount[i] == 0:
			canTake.append(i)
	classTake=[]
	while len(canTake) !=0:
		thisClass=canTake[0]
		del canTake[0]				#通过del删除队列的第i个元素
		classTake.append(thisClass)	 #针对thisClass做处理
		for i in range(numCourses):
			if preList[thisClass][i] ==1:	 
				#preList的第thisClass行为以thisClass为先修课的科目
				preListCount[i]-=1
				if preListCount[i] ==0: # 如果使得每一门课先修课为0的就加入队列
					canTake.append(i)
	return classTake