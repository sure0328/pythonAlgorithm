def twoSum(nums, target):
	res= []   				#存放结果编号数据
	newnums= nums[:]		#深拷贝，把原数据拷贝到newnums里
newnums.sort()			#对新数组排序
left = 0
right = len(newnums) - 1	#定义left和right指针分别指向新数组的开头和结尾
while left < right:
	if newnums[left] + newnums[right] == target:
      	for i in range(0,len(nums)):	#在原始数组中寻找第一个元素的原始下标
	         	if nums[i] == newnums[left]:
                    res.append(i)			#下标加入到结果集
                    break
     		for i in range(len(nums)-1,-1,-1):   #在原始数组中寻找第二个元素的原始下标
                if nums[i] == newnums[right]:
                    res.append(i)			#下标加入到结果集
                    break
          res.sort()
          break 
     elif newnums[left] + newnums[right] < target:
            left = left + 1				#让left指针向右移动一位
     elif newnums[left] + newnums[right] > target:
            right = right - 1			#让right指针向左移动一位
	return (res[0]+1,res[1]+1)	#返回结果集