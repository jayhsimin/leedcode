class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        解題思路:
        1. 將四個數組分成兩組來處理,可以降低時間複雜度
        2. 第一組: nums1和nums2的所有可能和及其出現次數存入字典
        3. 第二組: nums3和nums4的所有可能和的相反數若在字典中存在,則找到一組解
        """
        # 創建字典來存儲nums1和nums2中的元素和及其出現次數
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                # 計算n1和n2的和,並記錄在字典中
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1  # 如果和已存在,次數加1
                else:
                    hashmap[n1+n2] = 1   # 如果和不存在,初始化為1
        
        # 遍歷nums3和nums4,尋找能與hashmap中的值相加為0的組合
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4  # 計算相反數
                if key in hashmap:  # 如果相反數存在於hashmap中
                    count += hashmap[key]  # 將對應的組合數量加入結果
        return count
A = [ 0, 1]
B = [ 0, 0]
C = [ 0, 1]
D = [ 0, 0]
sol=Solution()
a=sol.fourSumCount(A,B,C,D)
print(a)
 
