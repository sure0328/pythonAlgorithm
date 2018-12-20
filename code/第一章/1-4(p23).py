n = int(input("Enter a number:"))			#输入一个数字
result = 1								#定义一个用于存储结果的变量
for i in range(1,n+1):						#循环时i的值从1到n
	result *= i							#当前的result乘上i
print(result)
