from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # 定义target在左闭右开的区间里，即：[left, right)

        while left < right:  # 因为left == right的时候，在[left, right)是无效的空间，所以使用 <
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle  # target 在左区间，在[left, middle)中
            elif nums[middle] < target:
                left = middle + 1  # target 在右区间，在[middle + 1, right)中
            else:
                return middle  # 数组中找到目标值，直接返回下标
        return -1  # 未找到目标值
# a=Solution.search([2,5,9,7,8,9,10],9)
# print(a)

result = Solution().search([2, 5, 7, 8, 9, 10], 9)
print(result)


# 在左闭右开区间的实现中，middle 不需要减 1 是因为在这种区间定义里，right 本身是不包含的，即 [left, right)。以下是详细的原因和原理：

# 左闭右开区间的特点
# 定义：

# 区间是 [left, right)，包括 left，但不包括 right。
# nums[middle] 是合法下标，而 right 永远不会被访问。
# 更新右边界：

# 当 nums[middle] > target 时，目标值在左区间，区间更新为 [left, middle)。
# 因为区间右端 right 是开区间，直接更新为 middle 就自动排除了 middle。
# 为什么不需要减 1？
# 更新右边界的逻辑：
# 假设 nums = [1, 3, 5, 7]，target = 3，初始区间 [0, 4)。
# 第一轮计算：
# middle = (0 + 4) // 2 = 2，nums[middle] = 5 > 3。
# 更新右边界：right = middle = 2。
# 区间变为 [0, 2)，此时 nums[2] 被排除。
# 因为 right 本身就是开区间，不包含在区间中，middle - 1 的调整是多余的。
# 如果减 1 会发生什么？
# 如果你写成 right = middle - 1，会错误地排除掉比 middle 更左边的值，导致漏检。
# 这是因为左闭右开的区间规则已经保证 right 的值是排除的。