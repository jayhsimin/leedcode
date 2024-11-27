from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 根据list的先进排序在先原则
        # 将nums的平方按从大到小的顺序添加进新的list
        # 最后反转list
        new_list = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                new_list.append(nums[right] ** 2)
                print(f"添加 {nums[right] ** 2} 来自 nums[{right}]")
                right -= 1
            else:
                new_list.append(nums[left] ** 2)
                print(f"添加 {nums[left] ** 2} 来自 nums[{left}]")
                left += 1
            print(f"当前新列表: {new_list}")
        result = new_list[::-1]
        print(f"最终结果（反转后）: {result}")
        return result
    
a=[-4,0,4,6,8]
ss=Solution()
o=ss.sortedSquares(a)
print(o)