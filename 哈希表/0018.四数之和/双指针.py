from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 對數組進行排序，以便後續操作
        nums.sort()
        n = len(nums)
        result = []
        # 遍歷數組中的每個數字，作為四數之和中的第一個數
        for i in range(n):
            # 剪枝：如果當前數字已經大於目標值，且都是正數，則後續不可能有合適的組合
            if nums[i] > target and nums[i] > 0 and target > 0:
                break
            # 去重：避免選取相同的第一個數字
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 選取第二個數字
            for j in range(i+1, n):
                # 剪枝：如果前兩個數字之和已經大於目標值，且都是正數，則後續不可能有合適的組合
                if nums[i] + nums[j] > target and target > 0:
                    break
                # 去重：避免選取相同的第二個數字
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # 使用雙指針法尋找合適的第三個和第四個數字
                left, right = j+1, n-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    # 如果四數之和等於目標值，則將組合加入結果中
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # 去重：避免選取相同的第三個數字
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        # 去重：避免選取相同的第四個數字
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    # 如果四數之和小於目標值，則移動左指針以增大總和
                    elif s < target:
                        left += 1
                    # 如果四數之和大於目標值，則移動右指針以減小總和
                    else:
                        right -= 1
        return result
