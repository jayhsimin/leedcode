from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #创建一个集合来存储我们目前看到的数字
        seen = set()             
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)