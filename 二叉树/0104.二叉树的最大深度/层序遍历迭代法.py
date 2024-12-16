import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        # 初始化一个双端队列，队列中的第一个元素是根节点
        queue = collections.deque([root])
        
        # 这段代码使用层序遍历的方法来计算二叉树的最大深度。
        # 使用一个队列来存储每一层的所有节点。对于队列中的每个节点，我们检查它的左右子节点。
        # 如果子节点存在，则将其加入队列中。每完成一层的遍历，深度计数器增加1。
        while queue:
            depth += 1  # 每遍历完一层，深度加1
            for _ in range(len(queue)):  # 遍历当前层的所有节点
                node = queue.popleft()  # 从队列中取出节点
                if node.left:  # 如果左子节点存在，加入队列
                    queue.append(node.left)
                if node.right:  # 如果右子节点存在，加入队列
                    queue.append(node.right)
        
        return depth
