from collections import defaultdict 
class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        """
        解題思路:
        1. 使用defaultdict來存儲nums1和nums2的元素和及其出現次數
        2. defaultdict的好處是當key不存在時會自動創建並賦予默認值0
        3. 將四個數組分成兩組處理,降低時間複雜度至O(n^2)
        """
        # 創建defaultdict來記錄nums1和nums2中元素和的出現次數
        rec = defaultdict(lambda : 0)
        cnt = 0  # 計數器,記錄符合條件的組合數
        
        # 計算nums1和nums2所有可能的和,並記錄在rec中
        for i in nums1:
            for j in nums2:
                rec[i+j] += 1  # 將和的出現次數加1
        
        # 遍歷nums3和nums4,查找能與rec中的值相加為0的組合
        for i in nums3:
            for j in nums4:
                # 查找-(i+j)在rec中的出現次數,如果不存在則返回0
                cnt += rec.get(-(i+j), 0) 
        
        return cnt