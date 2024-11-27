from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        
        # 迴圈開始
        while l <= r:
            # 比較左右邊界的平方值
            if nums[l] ** 2 < nums[r] ** 2: 
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
            
            # 輸出當前狀態
            print(f"當前狀態: l={l}, r={r}, i={i}, res={res}")
        
        return res