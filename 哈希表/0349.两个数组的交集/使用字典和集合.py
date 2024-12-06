from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用哈希表存储 nums1 的所有元素
        table = {}
        for num in nums1:
            # 如果 num 已存在於 table，累加其出現次數（不影響邏輯，主要是初始化值）
            table[num] = table.get(num, 0) + 1

        # 使用集合存储结果，避免重複元素
        res = set()
        for num in nums2:
            # 如果 num 存在於 table（表示兩個數組都有該數字）
            if num in table:
                res.add(num)  # 加入到結果集合中
                del table[num]  # 刪除該數字，避免重複計算

        # 將集合轉換為列表，返回結果
        return list(res)

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
print(solution.intersection(nums1, nums2))  # Output: [9, 4] (順序無關)

# 測試 4：空數組
nums1 = []
nums2 = [1, 2, 3]
print(solution.intersection(nums1, nums2))  # Output: []
