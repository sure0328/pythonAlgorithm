class TreeNode(object): 		#定义二叉树的根节点为TreeNode
	def __init__(self, x):
	     self.val = x			#定义二叉树的每个元素的值，这里表示草莓的编号
	     self.left = None		#定义二叉树的每个元素的左子树
	     self.right = None 		#定义二叉树的每个元素的右子树

def rightSide(root):
 result = []						#存放结果数据
 queue = [root]					#队列存放待处理数据
 while len(queue)>0:				#队列存放待处理数据
     length = len(queue)			#队列存放待处理数据
     for i in range(length):			#依次处理每一行
         node=queue.pop()			#取出队列头的点
         if i==length-1:				#当该点是最后一个点的时候把他加入到结果数组里
             result.append(node.val)
         if node.left !=None:
             queue.append(node.left)	#把左节点加入队列
         if node.right !=None:
             queue.append(node.right)	#把右节点加入队列
 return result

node1=TreeNode(1)					#以下为测试代码
node2=TreeNode(2)
node3=TreeNode(3)
node1.right=node2
node2.right=node3

print(rightSide(node1))