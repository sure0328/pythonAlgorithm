def Apple(n):				#函数Apple内n为购买的苹果个数
	if float(n//5) < n/5:			#a//b指a除以b的商的整数部分
		box = n//5 + 1		#box存储需要盒子的个数，box不能是小数，所以要+1
	else:
		box = n//5
	print("Price of apples:",2*n+box)  	#输出苹果总价
	return 2*n+box

def Pineapple(n):			#函数Pineapple内n为购买的菠萝个数
	print("Price of pineapples:",8*n+n)	#输出菠萝总价
	return 8*n+n

def Watermelon(n):			#函数Pineapple内n为购买的菠萝个数
    print("Price of watermelons:",10*n+n)	#输出西瓜总价
    return 10*n+n


numA = int(input("Enter the number of apples:"))
numP = int(input("Enter the number of pineapples:"))
numM = int(input("Enter the number of watermelons:"))
print("Total:",Apple(numA)+Pineapple(numP)+Watermelon(numM)) #三个函数返回值的和