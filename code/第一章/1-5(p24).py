count = 0
while True:
    if count%5 == 0:			 #如果count是5的倍数
        count += 1				 #count的值+1
        continue                #跳过这次循环进入下一次
    elif count == 12:           #如果count的值为12
        break                   #跳出这个循环
    print(count)
    count += 1