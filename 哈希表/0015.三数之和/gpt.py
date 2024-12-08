def threeSum(nums):
    # 结果存储列表
    res = []
    # 排序数组
    nums.sort()
    # 遍历数组
    for i in range(len(nums) - 2):
        # 跳过重复元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 初始化双指针
        left, right = i + 1, len(nums) - 1
        # 双指针查找
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                # 找到一个解
                res.append([nums[i], nums[left], nums[right]])
                # 跳过重复元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 移动指针
                left += 1
                right -= 1
            elif total < 0:
                # 总和小于 0，左指针右移
                left += 1
            else:
                # 总和大于 0，右指针左移
                right -= 1
    return res
