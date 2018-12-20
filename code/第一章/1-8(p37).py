numbers = []								#定义一个空列表
result = 1									#定义一个变量用于存储结果
total = int(input("Enter the amount of numbers:"))	#输入列表内要有多少个整数
for i in range(total):							#用for循环把元素加入进列表
	numbers.append(int(input("Enter a number:")))
for i in numbers:							#用for把列表的每个元素与result相乘
	result *= i								#i为列表的每个元素本身
print(result)