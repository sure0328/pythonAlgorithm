def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        m = nums[i]  # 定义m为当前待查询数字
        if target - m in dict:  # 判定target-m是否已经在字典之中
            return (dict[target - m] + 1, i + 1)  # 如果已经存在，则返回这两个数的下标回来
        dict[m] = i  # 如果不存在则记录键值对
