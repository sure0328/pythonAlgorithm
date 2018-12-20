born_year = int(input("Enter the year you born:"))			#输入出生年份
this_year = int(input("Enter this year:"))					#输入今年
while born_year > this_year:							#当出生年份大于今年时循环
	print("Your age can’t be negative. Please enter again.")
	born_year = int(input("Enter the year you born:"))		#再次输入
	this_year = int(input("Enter this year:"))
else:												#循环结束，数据合法
	print("Input success.")
print("Your age is", this_year - born_year)					#输出结果