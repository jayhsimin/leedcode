# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self, cur: TreeNode, count: int) -> bool:
        # 這是輔助函式，透過遞迴遍歷樹，檢查是否存在目標和的路徑。cur 表示當前節點，count 表示剩餘需要達成的總和。
        if not cur.left and not cur.right and count == 0: # 遇到叶子节点，并且计数为0
            return True
        if not cur.left and not cur.right: # 遇到叶子节点直接返回
            return False
        
        if cur.left: # 左
            count -= cur.left.val
            if self.traversal(cur.left, count): # 递归，处理节点
                return True
            count += cur.left.val # 回溯，撤销处理结果
            
        if cur.right: # 右
            count -= cur.right.val
            if self.traversal(cur.right, count): # 递归，处理节点
                return True
            count += cur.right.val # 回溯，撤销处理结果
            
        return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.traversal(root, targetSum - root.val)      