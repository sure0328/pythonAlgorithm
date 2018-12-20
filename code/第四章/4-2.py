class Solution:
    def maxPathSum(self, root):				#输出最大路径和的方法
        return max(self.helper(root))		#调用helper方法，传入根节点，输出返回的两个值的最大值
    def helper(self, root):				#helper方法，输出一个二维数组 [ 不停值，停值 ]
        if root==None:				#如果节点为空，输出两个最小值
            return float('-int'), float('-int')
        leftY,leftN = self.helper(root.left)			#得到左子节点的不停值与停值
        rightY,rightN = self.helper(root.right)		#得到右子节点的不停值与停值
        yes = max(root.val+leftY,root.val+rightY,root.val)			#不停值
        no = max(leftN,rightN,leftY,rightY,root.val+leftY+rightY) 		#停值
        return yes,no					#输出 [ 不停值，停值 ]