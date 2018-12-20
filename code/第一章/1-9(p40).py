def Plus(a,b):
	print(a+b)

def Hello():
	num1 = int(input("Hello! Please enter the first number:"))
	num2 = int(input("Please enter the second number:"))
	return num1,num2

n1,n2 = Hello()
Plus(n1,n2)