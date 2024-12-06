from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用集合的交集操作來快速找到兩個數組的交集
        return list(set(nums1) & set(nums2))
solution = Solution()

# 測試 1：一般情況
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersection(nums1, nums2))  # Output: [2]

# 測試 2：完全不同的數組
nums1 = [4, 5, 6]
nums2 = [1, 2, 3]
print(solution.intersection(nums1, nums2))  # Output: []

# 測試 3：有多個交集元素
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(solution.intersection(nums1, nums2))  # Output: [9, 4] (順序可能不同)

# 測試 4：空數組
nums1 = []
nums2 = [1, 2, 3]
print(solution.intersection(nums1, nums2))  # Output: []

# 測試 5：範圍極限
nums1 = [0, 1000]
nums2 = [1000, 0, 500]
print(solution.intersection(nums1, nums2))  # Output: [0, 1000]
