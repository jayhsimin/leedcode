from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # 檢查空數組
            return 0

        low = 0  # 用於記錄唯一元素的位置
        for fast in range(1, len(nums)):
#range 是否以 0 開始，會根據程式的需求有所影響。在你的程式中，range(1, len(nums)) 是正確的選擇，因為我們使用雙指針法時，low 和 fast 初始值分別對應到數組的第一個元素（索引 0），因此不需要在第一個元素上重複判斷。
# 為什麼 range(1, len(nums)) 合適？
# fast 從索引 1 開始：
# 第一個元素 (nums[0]) 本身就是唯一的，沒有必要比較自己和自己。
# 從索引 1 開始比較，是為了檢查後續的元素是否和 nums[low] 不同。
# 如果用 range(0, len(nums))：
# fast 從索引 0 開始，nums[fast] == nums[low]，這會在第一輪多做一次無意義的比較。
# 程式依然會正確運作，但效率稍低。
            if nums[fast] != nums[low]:  # 當發現一個新元素
                low += 1                # 移動 low 指針
                nums[low] = nums[fast]  # 將新元素移到 low 位置

        return low + 1  # 返回唯一元素的個數
    # 因為low是索引值，所以需要+1

# 測試
nums = [1, 1, 2, 2, 3]
solution = Solution()
k = solution.removeDuplicates(nums)
print("唯一元素的數量:", k)
print("修改後的數組:", nums[:k])
