import collections
# 定义二叉树节点的类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点
# 解决方案类
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 如果根节点为空，则返回0，因为树的深度为0
        if not root:
            return 0
        depth = 0  # 初始化树的深度为0
        queue = collections.deque([root])  # 初始化队列，包含根节点
        
        while queue:  # 当队列不为空时
            depth += 1  # 每次循环，树的深度增加1
            for _ in range(len(queue)):  # 遍历当前队列中的所有节点
                node = queue.popleft()  # 从队列中取出一个节点
                
                # 如果当前节点是叶子节点（即没有左子节点和右子节点），返回当前树的深度
                if not node.left and not node.right:
                    return depth
            
                # 如果当前节点有左子节点，则将左子节点加入队列
                if node.left:
                    queue.append(node.left)
                    
                # 如果当前节点有右子节点，则将右子节点加入队列
                if node.right:
                    queue.append(node.right)

        # 如果队列为空，返回当前树的深度
        return depth