class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        解題思路:
        1. 將四個數組分成兩組來處理,可以降低時間複雜度
        2. 第一組: nums1和nums2的所有可能和及其出現次數存入字典
        3. 第二組: nums3和nums4的所有可能和的相反數若在字典中存在,則找到一組解
        時間複雜度: O(n^2), 空間複雜度: O(n^2)
        """
        # 創建字典來存儲nums1和nums2中的元素和及其出現次數
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                # 計算n1和n2的和,如果和已存在則加1,不存在則初始化為1
                hashmap[n1+n2] = hashmap.get(n1+n2, 0) + 1
# 這部分使用了字典的 get() 方法。get(key, default) 會返回指定 key 的值。
# 如果字典中存在 key，則返回該 key 對應的值；如果字典中不存在該 key，
# 則返回 default 參數指定的值。
# 在這裡，n1 + n2 是 key，如果 n1 + n2 在 hashmap 中存在，
# 那麼 get() 方法就會返回 hashmap[n1 + n2] 的值，即該和出現的次數。
# 如果 n1 + n2 不在 hashmap 中，get() 就會返回 0，也就是說，默認它的出現次數是 0。
        
        # 遍歷nums3和nums4,尋找能與hashmap中的值相加為0的組合
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                # 計算n3和n4的和的相反數
                key = - n3 - n4
                # 如果相反數存在於hashmap中,將對應的組合數量加入結果
                if key in hashmap:
                    count += hashmap[key]
        return count
