from typing import Optional

# 節點定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 輔助函數：將鏈表轉為字符串，便於打印
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

# 解決方案
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 建立虛擬頭節點
        dummy_head = ListNode(next=head)
        
        # 遍歷刪除節點
        current = dummy_head
        while current.next:
            if current.next.val == val:#獲取下一個節點的值，判斷是否需要刪除。
                current.next = current.next.next#用於刪除下一個節點，讓當前節點直接指向下一個的下一個。
            else:
                current = current.next
        
        return dummy_head.next#由於原始的 head 可能已被刪除，必須通過 dummy_head.next 獲取新的頭節點。

# 測試輔助函數
def build_linked_list(values):
    """根據列表構建鏈表"""
    dummy_head = ListNode()
    current = dummy_head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

# 測試程式碼
if __name__ == "__main__":
    # 輸入鏈表和目標值
    values = [1, 2, 6, 3, 4, 5, 6]
    val_to_remove = 6
    head = build_linked_list(values)

    print("原始鏈表:", head)

    # 移除目標值節點
    solution = Solution()
    new_head = solution.removeElements(head, val_to_remove)

    print("移除後的鏈表:", new_head)
