from typing import List 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        整体思想：有序数组的绝对值最大值永远在两头，比较两头，平方大的插到新数组的最后
        优   化：1. 优化所有元素为非正或非负的情况
                2. 头尾平方的大小比较直接将头尾相加与0进行比较即可
                3. 新的平方排序数组的插入索引可以用倒序插入实现（针对for循环，while循环不适用）
        """
 
        # 特殊情况, 元素都非负（优化1）
        if nums[0] >= 0:
            return [num ** 2 for num in nums]  # 按顺序平方即可
        # 最后一个非正，全负有序的
        if nums[-1] <= 0:
            return [x ** 2 for x in nums[::-1]]  # 倒序平方后的数组
        
        # 一般情况, 有正有负
        i = 0  # 原数组头索引
        j = len(nums) - 1  # 原数组尾部索引
        new_nums = [0] * len(nums)  # 新建一个等长数组用于保存排序后的结果
        # end_index = len(nums) - 1  # 新的排序数组(是新数组)尾插索引, 每次需要减一（优化3优化了）

        for end_index in range(len(nums)-1, -1, -1): # (优化3，倒序，不用单独创建变量)
            # if nums[i] ** 2 >= nums[j] ** 2:
            if nums[i] + nums[j] <= 0:  # (优化2)
                new_nums[end_index] = nums[i] ** 2
                i += 1
                end_index -= 1  #(优化3)
            else:
                new_nums[end_index] = nums[j] ** 2
                j -= 1
                end_index -= 1  #(优化3)
        return new_nums
a=[-4,0,4,6,8]
ss=Solution()
o=ss.sortedSquares(a)
print(o)