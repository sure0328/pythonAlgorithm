value = 0					#预先设置好值和指针在小数组中的位置
pointer = 1
LinkedList = [ [1,3], [5,2], [6,-1], [2,5], [4,1], [3,4] ]
head = 0
print(LinkedList[head][value])	#直接输出第一个元素的值
next = LinkedList[head][next]	#给next赋初始值

while next != -1:		#next是指向下一个元素的指针，它不等于-1代表后面还有元素
	print(LinkedList[next][value])	#输出下一个元素中存储的值
next = LinkedList[next][pointer]	#把指针变为下一个元素中存储的指针