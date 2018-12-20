numA = int(input("Enter the number of apples:"))	#输入
numP = int(input("Enter the number of pineapples:"))
numM = int(input("Enter the number of watermelons:"))

if numA//5 < numA:				#a//b指a除以b的商的整数部分
	box = numA//5 + 1			#box存储需要盒子的个数，box不能是小数，所以要+1
else:
	bag = numA//5
sumA = 2*numA + box			#sumA用于存储苹果总价
print("Price of apples:",sumA)		#输出苹果总价
sumP = 8*numP + numP			#sumP用于存储菠萝总价
print("Price of pineapples:",sumP)	#输出菠萝总价
sumM = 8*numM + numM			#sumM用于存储西瓜总价
print("Price of pineapples:",sumM)	#输出西瓜总价
print("Total:",sumA+sumP+sumM)