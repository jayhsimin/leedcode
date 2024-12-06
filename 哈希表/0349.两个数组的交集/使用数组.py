from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用固定大小的計數器陣列，假設數字範圍在 [0, 1000]
        count1 = [0] * 1001
        count2 = [0] * 1001
        result = []

        # 計算 nums1 中每個數字的出現次數
        for num in nums1:
            count1[num] += 1

        # 計算 nums2 中每個數字的出現次數
        for num in nums2:
            count2[num] += 1

        # 遍歷數字範圍，找出兩個數組中都出現的數字
        for num in range(1001):
            if count1[num] > 0 and count2[num] > 0:  # 兩個陣列中該數字都出現
                result.append(num)

        return result
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
print(solution.intersection(nums1, nums2))  # Output: [4, 9]

# 測試 4：空數組
nums1 = []
nums2 = [1, 2, 3]
print(solution.intersection(nums1, nums2))  # Output: []

# 測試 5：範圍極限
nums1 = [0, 1000]
nums2 = [1000, 0, 500]
print(solution.intersection(nums1, nums2))  # Output: [0, 1000]
