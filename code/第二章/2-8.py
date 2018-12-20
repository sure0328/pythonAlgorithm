def Output(ListValue,ListRight,head):		#定义一个函数用于输出链表
	print(ListValue[head])
	next = ListRight[head]
	while next != -1:
		print(ListValue[next])
		next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]				#建立一个双链表
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]
head = 0								#确定第一个元素的位置
prepos = 5							#确定要插入的位置的前一个元素的位置

Output(ListValue,ListRight,head)			#输出未经插入的链表
print()

ListValue.append(4)						#在ListValue数组末尾加上新元素的值
ListRight.append(ListRight[prepos])			#给新元素的两个指针赋值
ListLeft.append(prepos)
ListLeft[ListRight[prepos]] = len(ListValue)-1	#前后元素的指针指向新元素
ListRight[prepos] = len(ListValue)-1		

Output(ListValue,ListRight,head)			#输出插入后的链表