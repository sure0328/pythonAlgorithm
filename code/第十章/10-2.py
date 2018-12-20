def mergeSort(myList):								#传入参数myList
    length = len(myList)     							#myList的长度
    n = 1									#n为子数组长度，初始值为1
    while n <length:							#如果子数组长度小于myList的长度
      for i in range(0,length,n*2):					#利用for loop把子数组成对排序
        listA = myList[i:i+n]						#listA与listB为一对长度为n的子数组
        listB = myList[i+n:i+n*2]
        pointerA = 0							#利用指针将listA与listB排序
        pointerB = 0
       	counter = i
        while (pointerA<len(listA) and pointerB <len(listB)):
           if(listA[pointerA]<listB[pointerB]):
             myList[counter]=listA[pointerA]
             pointerA+=1
           else:
             myList[counter]=listB[pointerB] 
             pointerB+=1
           counter+=1
        while pointerA<len(listA):				
           myList[counter]=listA[pointerA]			
           pointerA+=1
           counter+=1
        while pointerB<len(listB):				
           myList[counter]=listB[pointerB] 				
           pointerB+=1
           counter+=1
        n=n*2									#将n乘2
listX = [-2,9,0,8,5,-4,8]
mergeSort(listX)
print(listX)