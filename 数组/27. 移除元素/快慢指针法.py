from typing import List

def removeElement(nums: List[int], val: int) -> int:
    """
    使用快慢指针法移除数组中的指定元素

    参数:
    nums (List[int]): 整数数组
    val (int): 需要移除的元素值

    返回:
    int: 移除指定元素后的数组新长度

    详细说明:
    1. 初始化快指针 (fast) 和慢指针 (slow) 都为 0。
    2. 遍历数组，快指针用于遍历每一个元素。
    3. 如果快指针指向的元素不等于 val，则将该元素赋值给慢指针指向的位置，并将慢指针加 1。
    4. 快指针每次循环都加 1。
    5. 最终返回慢指针的值，即为移除指定元素后的数组新长度。

    示例:
    输入: nums = [3,2,2,3], val = 3
    输出: 2, nums = [2,2]
    """
    fast = 0  # 快指针
    slow = 0  # 慢指针
    size = len(nums)
    while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
        # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow