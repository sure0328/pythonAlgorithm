ListValue = [1, 5, 6, 2, 7, 3]	#第一种模拟双链表的方法
ListRight = [3, 2, 4, 5, -1, 1]	#分别使用三个数组来存储数值、
ListLeft = [-1, 5, 1, 0, 2, 3]		#指向上一个元素和下一个元素的指针

head = ListLeft.index(-1)		#头指针的值为-1在ListLeft中的位置
print(ListValue[head])
Next = ListRight[head]	

while Next > -1:
	print(ListValue[Next])
	Next = ListRight[Next]
print()	    				#换行隔开两个链表的输出结果
right = 1					#第二种模拟双链表的方法
left = 2
value = 0
LinkedList = [[1, 3, -1], [5, 2, 5], [6, 4, 1], [2, 5, 0], [7, -1, 2], [3, 1, 3]]
head = 0					#提前设置头指针指向的位置
print(LinkedList[head][value])
Next = LinkedList[head][right]

while Next > -1:
	print(LinkedList[Next][value])
	Next = LinkedList[Next][right]