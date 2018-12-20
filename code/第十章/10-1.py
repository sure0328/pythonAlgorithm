def mergeSort(myList):						#传入参数myList
     if len(myList)<2:							#如果myList只有一个元素，终止
       return
     cut = len(myList)//2						#找到列表中点
     listA = myList[:cut]						#左子列表
     listB = myList[cut:]						#右子列表
     mergeSort(listA)							#把左子列表归并排序
     mergeSort(listB)							#把右子列表归并排序
     pointerA = 0								#指针A
     pointerB = 0								#指针B
     counter=0								#定义一个counter
     while (pointerA<len(listA) and pointerB <len(listB)):	#如果两个指针都没走到头
       if(listA[pointerA]<listB[pointerB]):				#比子列表元素大小
         myList[counter]=listA[pointerA]				#小的元素替换myList[counter]
         pointerA+=1								#移动指针
       else:
         myList[counter]=listB[pointerB] 
         pointerB+=1
       counter+=1								#counter加一
     while pointerA<len(listA):					#如果指针B走到头了但指针A没有
       myList[counter]=listA[pointerA]				#指针A对应的元素替换myList[counter]
       pointerA+=1
       counter+=1
     while pointerB<len(listB):					#如果指针A走到头了但指针B没有	
       myList[counter]=listB[pointerB] 				#指针B对应的元素替换myList[counter]
       pointerB+=1
       counter+=1
listX = [2,3,4,1,3,0]							
mergeSort(listX)
print(listX)