from typing import List, Optional

# 定义二叉树的节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 当前节点的值
        self.left = left  # 左子树
        self.right = right  # 右子树

def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    """
    根据给定的数组构建最大二叉树
    :param nums: 不含重复元素的整数数组
    :return: 最大二叉树的根节点
    """
    # 递归终止条件：数组为空
    if not nums:
        return None

    # 找到当前数组中的最大值及其索引
    max_value = max(nums)  # 最大值
    max_index = nums.index(max_value)  # 最大值的索引，用于分割数组

    # 创建当前子树的根节点
    root = TreeNode(val=max_value)

    # 构建左子树，数组范围是最大值左边部分
    root.left = constructMaximumBinaryTree(nums[:max_index])

    # 构建右子树，数组范围是最大值右边部分
    root.right = constructMaximumBinaryTree(nums[max_index + 1:])

    # 返回构建好的子树根节点
    return root

def printTree(root: Optional[TreeNode], level=0, prefix="Root: "):
    """
    辅助函数：按树形结构打印二叉树
    :param root: 二叉树根节点
    :param level: 当前节点所在的层级
    :param prefix: 当前节点的前缀（用于标识当前是左子树或右子树）
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))  # 打印当前节点的值，并根据层级进行缩进
        if root.left or root.right:  # 如果有子节点
            if root.left:
                printTree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                printTree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# 测试用例
nums = [3, 2, 1, 6, 0, 5]  # 示例数组
root = constructMaximumBinaryTree(nums)  # 构建最大二叉树
printTree(root)  # 打印结果
