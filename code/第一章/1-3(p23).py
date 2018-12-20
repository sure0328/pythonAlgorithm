n = int(input("Enter a number:"))			#输入一个数字
count = 1								#定义一个用于计数的变量
result = 1								#定义一个用于存储结果的变量
while count <= n:						#当count小于等于n时循环
	result *= count						#当前的result乘上count
	count += 1							#更新count的值
print(result)