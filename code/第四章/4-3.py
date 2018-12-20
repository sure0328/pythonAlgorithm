class Solution(object): 	
	def maxAreaOfIsland(self, grid):
        self.maxArea= 0			#存储最大岛屿的面积
        row = len(grid)			#存储地图的行数
        col = len(grid[0])			#存储地图的列数
        for i in range(row):
            for j in range(col):	#开始从左到右，从上到下的搜索岛屿	
                if grid[i][j] == 1:	#如果发现了陆地的话
                    current = 1
                    self.dfs(i, j, current, grid)   #测量岛屿面积，核心代码
        return self.maxArea		#最后返回最大岛屿的
    def dfs(self, k, z, current, grid):			
	# k,z为点的坐标
	#current存储目前岛屿的面积，grid为地图
        grid[k][z] = 2						#第一步先标记此处为已访问
        if k > 0 and grid[k-1][z] == 1:			#向上走前先考察不越界并且为陆地
               current= self.dfs(k-1, z, current+1, grid)	#递归调用函数，更新x左边和当前面积
        if k < (len(grid)-1) and grid[k+1][z] == 1:	#向下走前先考察不越界并且为陆地
               current= self.dfs(k+1, z, current+1, grid)
        if z > 0 and grid[k][z - 1] == 1:			#向左走前先考察不越界并且为陆地
               current= self.dfs(k, z-1, current+1, grid)
        if z < (len(grid[0])-1) and grid[k][z+1] == 1:	#向右走前先考察不越界并且为陆地
              current= self.dfs(k, z+1, current+1, grid)
        self.maxArea= max(self.maxArea, current)	#更新最大面积变量
        return current