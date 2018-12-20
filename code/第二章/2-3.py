ListValue = [1,5,6,2,4,3]
ListPointer = [3,2,-1,5,1,4]
head = 0					#head是指向链表第一个元素的指针，需要自己定义
print(ListValue[head])		#直接输出第一个元素的值
next = ListPointer[head]		#给next赋初始值
while next != -1:			#next是指向下一个元素的指针，不等于-1代表后面还有元素
	print(ListValue[next])		#输出下一个元素中存储的值
	next = ListPointer[next]	#把指针变为下一个元素中存储的指针