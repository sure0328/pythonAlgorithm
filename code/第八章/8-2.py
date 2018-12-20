def goldMining(n, w, g, p):
	results = []					#保存返回结果的数组
	preResults = []				#保存上一行结果的数组
	for i in range(0,w):			#填充边界格子的值，从左向右填充表格第一行的内容
		results.append(0)		#初始化结果数组
		if  i < p[0]:	
			preResults.append(0)	#若人数少于第一个金矿所需人数，黄金量为0
		else:
			preResults.append(g[0])	#若人数不少于第一个金矿所需人数，黄金量为g[0]

	for i in range(0,n):			#外层循环为金矿数量
		for j in range(0,w):		#外层循环为矿工数量
			if j < p[i]:
				results[j] = preResults[j]
			else:
				results[j] = Math.max(preResults[j], preResults[j-p[i]] + g[i])
		preResults = results
	return results