def Output(ListValue,ListRight,head):			#输出函数
    print(ListValue[head])
    n = ListRight[head]
    while n != -1:
        print(ListValue[n])
        n = ListRight[n]

ListValue = [1, 5, 6, 2, 7, 3]					#建立单链表
ListRight = [3, 2, 4, 5, -1, 1]
head = 0									#确定头指针
prepos = 5								#确定要删除的元素的前一个数的位置

Output(ListValue, ListRight, head)				#输出删除前的链表
print()

ListRight[prepos] = ListRight[ListRight[prepos]]		#删除元素

Output(ListValue, ListRight, head)				#输出删除后的链表