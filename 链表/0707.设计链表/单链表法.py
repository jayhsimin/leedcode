class ListNode:
    """
    定义链表节点类。
    """
    def __init__(self, val=0, next=None):
        self.val = val  # 节点的值
        self.next = next  # 指向下一个节点的指针

class MyLinkedList:
    """
    定义链表类，实现各种链表操作。
    """
    def __init__(self):
        """
        初始化链表。
        使用一个哑节点（dummy_head）简化边界操作。
        初始链表大小为0。
        """
        self.dummy_head = ListNode()  # 哑节点，指向链表的起点
        self.size = 0  # 链表当前节点数

    def get(self, index: int) -> int:
        """
        获取链表中第 index 个节点的值。如果索引无效，则返回 -1。
        """
        if index < 0 or index >= self.size:  # 检查索引是否有效
            return -1
        
        # 从哑节点后的第一个节点开始遍历
        current = self.dummy_head.next
        for i in range(index):  # 遍历到第 index 个节点
            current = current.next
            
        return current.val  # 返回目标节点的值

    def addAtHead(self, val: int) -> None:
        """
        在链表头部插入一个值为 val 的节点。
        """
        # 创建新节点，指向原链表的第一个节点
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1  # 增加链表大小

    def addAtTail(self, val: int) -> None:
        """
        在链表尾部插入一个值为 val 的节点。
        """
        # 从哑节点开始，遍历到链表的尾部
        current = self.dummy_head
        while current.next:  # 循环到最后一个节点
            current = current.next
        # 创建新节点并链接到链表尾部
        current.next = ListNode(val)
        self.size += 1  # 增加链表大小

    def addAtIndex(self, index: int, val: int) -> None:
        """
        在链表中的第 index 个节点之前插入一个值为 val 的节点。
        如果 index 等于链表长度，则该节点将附加到链表的末尾。
        如果 index 大于链表长度，则不会插入节点。
        如果 index 小于0，则在头部插入节点。
        """
        if index < 0:  # 如果索引小于 0，在头部插入节点
            index = 0
        if index > self.size:  # 如果索引超出范围，不执行操作
            return
        
        # 从哑节点开始，遍历到目标位置的前一个节点
        current = self.dummy_head
        for i in range(index):
            current = current.next
        
        # 创建新节点并插入链表
        current.next = ListNode(val, current.next)
        self.size += 1  # 增加链表大小

    def deleteAtIndex(self, index: int) -> None:
        """
        删除链表中第 index 个节点，如果索引无效则不进行操作。
        """
        if index < 0 or index >= self.size:  # 检查索引是否有效
            return
        
        # 从哑节点开始，遍历到目标位置的前一个节点
        current = self.dummy_head
        for i in range(index):
            current = current.next
        
        # 删除目标节点
        current.next = current.next.next
        self.size -= 1  # 减少链表大小


# 使用示例
# 实例化链表
obj = MyLinkedList()
obj.addAtHead(1)       # 链表: 1
obj.addAtTail(3)       # 链表: 1 -> 3
obj.addAtIndex(1, 2)   # 链表: 1 -> 2 -> 3
print(obj.get(1))      # 输出: 2
obj.deleteAtIndex(1)   # 链表: 1 -> 3
print(obj.get(1))      # 输出: 3
