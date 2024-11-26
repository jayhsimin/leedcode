from typing import List
class Solution:
    # 直接平方再排序
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()  # 使用内置的sort()方法对数组进行排序。sort()方法是原地排序，不会创建新的列表，时间复杂度为O(n log n)。
        return nums