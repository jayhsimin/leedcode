class Solution:
    def __init__(self):
        self.result = float('inf')

    def getDepth(self, node, depth):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.result = min(self.result, depth)
        if node.left:
            self.getDepth(node.left, depth + 1)
        if node.right:
            self.getDepth(node.right, depth + 1)

    def minDepth(self, root):
        if root is None:
            return 0
        self.getDepth(root, 1)
        return self.result

