class TreeNode:
    def __init__(self,root=0,right=None,left=None):
        self.root=root
        self.right=right
        self.left=left
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)
        
    def getNodesNum(self, cur):
        if not cur:
            return 0
        leftNum = self.getNodesNum(cur.left) #递归计算左子树的节点数
        rightNum = self.getNodesNum(cur.right) #递归计算右子树的节点数
        treeNum = leftNum + rightNum + 1 #当前节点的节点数
        return treeNum