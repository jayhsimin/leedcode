from typing import List


# 定义二叉树的节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 当前节点的值
        self.left = left  # 左子树
        self.right = right  # 右子树


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    if not nums:
        return None
    max_val = max(nums)  # 找到当前数组的最大值
    max_index = nums.index(max_val)  # 找到最大值的索引
    # 创建根节点
    node = TreeNode(max_val)
    # 构建左子树
    node.left = constructMaximumBinaryTree(nums[:max_index])
    # 构建右子树
    node.right = constructMaximumBinaryTree(nums[max_index + 1:])
    return node


# 辅助函数：打印二叉树为树状结构
def print_tree_structure(node: TreeNode, level=0):
    if not node:
        return
    # 递归打印右子树
    print_tree_structure(node.right, level + 1)
    # 打印当前节点
    print(" " * 4 * level + f"- {node.val}")
    # 递归打印左子树
    print_tree_structure(node.left, level + 1)


# 测试用例
nums = [3, 2, 1, 6, 0, 5]  # 示例数组
root = constructMaximumBinaryTree(nums)  # 构建最大二叉树
print_tree_structure(root)  # 打印二叉树的树状结构
