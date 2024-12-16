import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: 
            return None

        queue = collections.deque([root])    
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            # 如果节点的左子节点存在，则将左子节点加入队列中
            if node.left: queue.append(node.left)
            # 如果节点的右子节点存在，则将右子节点加入队列中
            if node.right: queue.append(node.right)
        return root   

