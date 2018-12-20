num1 = int(input("Enter the dividend:"))
num2 = int(input("Enter the divider:"))
if num2 != 0:							#如果输入的除数不是0
	result = num1/num2
	if result == int(num1/num2):			#如果result的值与两数相除取整后的值相等
		print(int(result),"integer")
	else:
		print(result,"decimal")
else:
	print("The divider can’t be 0.Error.")