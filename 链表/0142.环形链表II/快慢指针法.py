
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()  # 创建一个空集合，用于存储访问过的节点
        
        while head:  # 遍历链表
            if head in visited:  # 如果当前节点已被访问过，说明找到了环的起点
                return head
            visited.add(head)  # 否则，将当前节点加入集合
            head = head.next  # 移动到下一个节点
        
        return None  # 如果遍历完整个链表都没有找到环，返回 None
