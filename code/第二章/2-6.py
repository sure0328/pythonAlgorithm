ListValue = [1, 5, 6, 2, 7, 3]		#和第二小节一模一样的正向输出
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]

head = ListLeft.index(-1)
print(ListValue[head])
Next = ListRight[head]

while Next > -1:					
    print(ListValue[Next])
    Next = ListRight[Next]

head = ListRight.index(-1)			#从这里开始的是反向输出
print(ListValue[head])
Next = ListLeft[head]

while Next > -1:
    print(ListValue[Next])
    Next = ListLeft[Next]