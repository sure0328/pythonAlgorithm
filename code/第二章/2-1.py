arr1 = [1,3,4,6,10]					#初始化两个数组
arr2 = [2,5,8,11]
ind = 0
ans = arr1.copy()					#ans初始化为arr1
for i in range(0,len(arr2)):
	while ind < len(arr1):
		if arr2[i] <= arr1[ind]:			#ind的范围不能超过数组元素下标的最大值
			ans.insert(ind + i,arr2[i])	#向第一个数组中的合适位置插入第二个数组的数
			break
	else:
		ind += 1				#如果ind指向的数比i指向的数小，则ind向后一位
else:						#如果arr1已遍历完，直接把剩下的arr2拼到arr1结尾
	ans = ans + arr2[i:]
		break