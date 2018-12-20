def Output(ListValue,ListRight,head):	#定义一个函数用于输出链表
	print(ListValue[head])
	next = ListRight[head]
	while next != -1:
		print(ListValue[next])
		next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]		
ListRight = [3, 2, 4, 5, -1, 1]
head = 0
prepos = 5						#已知要插入的位置的上一个元素的位置

Output(ListValue,ListRight,head)		#输出未插入元素的链表
print()

ListValue.append(4)					#向数组末尾加上新元素的值4
ListRight.append(ListRight[prepos])		#加上新元素指针指向的位置（下一个元素）
ListRight[prepos] = len(ListValue)-1		#上一个元素的指针指向新元素

Output(ListValue,ListRight,head)		#输出已经插入元素的链表