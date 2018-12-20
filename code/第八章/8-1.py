a = 1						#初始化边界值
b = 2
temp = 0

def upstairs(n):
	if  n < 1:				#判断当前台阶级数小于1
		print(0)
	if  n == 1:				#判断当前台阶级数为1
		print(1)
	if  n == 2:				#判断当前台阶级数为2
		print(2)

	for i in range(3,n):		#迭代求解各级台阶的走法数量
		temp = a + b
		a = b
		b = temp
	print(temp)			#输出计算结果