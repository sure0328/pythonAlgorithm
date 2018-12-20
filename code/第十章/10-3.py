def maxSubArray(nums):				#传入参数nums列表
    if nums==[]:						#如果列表为空，终止
        return
    if len(nums)==1:					#如果列表只有一个元素，输出此元素
        return nums[0]
    cut = len(nums)//2					#设中点
    leftSum = maxSubArray(nums[:cut])	#分治：找到左子列表的最大和
    rightSum = maxSubArray(nums[cut:])	#找到右子列表的最大和
    leftMiddleSum=0
    maxL = 0
    rightMiddleSum=0
    maxR =0
    for i in range(cut-1,-1,-1):			#找到左子列表与右子列表之间的子列表的最大和
       leftMiddleSum+=nums[i]
       maxL = max(leftMiddleSum,maxL)
    for i in range(cut+1,len(nums),1):
       rightMiddleSum+=nums[i]
       maxR = max(rightMiddleSum,maxR)
    return(max(leftSum,maxL+nums[cut]+maxR,rightSum))		#返回三个可能的最大值
maxSum = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])			#示例
print(maxSum)