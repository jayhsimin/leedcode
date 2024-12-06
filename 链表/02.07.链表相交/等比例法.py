# 定義鏈表的節點類
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解決方案類
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况
        if not headA or not headB:
            return None
        
        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB
        
        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA


# 測試函數
def test():
    # 創建兩個鏈表
    # 鏈表A: 1 -> 2 -> 3 -> 4 -> 5
    # 鏈表B: 9 -> 3 -> 4 -> 5 (3 -> 4 -> 5 是交點)
    # common = ListNode(3)
    # common.next = ListNode(4)
    # common.next.next = ListNode(5)

    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(3)

    headB = ListNode(6)
    headB.next = ListNode(8)
    headB.next.next = ListNode(3)
    headB.next.next.next = ListNode(9)

    # 使用解法找交點
    solution = Solution()
    intersection = solution.getIntersectionNode(headA, headB)

    # 打印結果
    if intersection:
        print(f"交點的值: {intersection.val}")
    else:
        print("沒有交點")


# 執行測試
test()
