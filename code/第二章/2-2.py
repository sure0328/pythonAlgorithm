numbers = [1,3,5,6,7,8,13,14,15,17,18,24,30,43,56]
head,tail = 0, len(numbers)	#数组长度刚好是最大下标值+1
search = int(input("Enter a number to search:"))
	
while tail - head > 1:	#当尾指针tail减头指针head等于1时，查找范围内只head有指向的数
	mid = (head+tail)//2	#mid存储中间数的下标，//2代表对/2的结果舍去分数部分取整
	if search < numbers[mid]:  #search是我们要搜索的元素，如果它小于mid指向的元素
		tail = mid - 1
	if search > numbers[mid]:	  	#如果search小于mid指向的元素
		head = mid + 1		   #mid指向的元素小于search，所以不用把它保留在范围内
	if search == numbers[mid]:
		ans = mid
		break				#找到元素的话就直接结束
else:
	if search == numbers[head]:	
		ans = head			
	else:
		ans = -1				#如果数组中没有这个元素，那么输出-1
print(ans)