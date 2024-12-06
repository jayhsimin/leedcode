class ListNode:
    """
    定义链表节点类。
    每个节点包含值 val，以及指向前一个和后一个节点的指针 prev 和 next。
    """
    def __init__(self, val=0, prev=None, next=None):
        self.val = val  # 节点的值
        self.prev = prev  # 指向前一个节点的指针
        self.next = next  # 指向后一个节点的指针

class MyLinkedList:
    """
    定义双向链表类，实现题目中要求的操作。
    """
    def __init__(self):
        """
        初始化双向链表，初始状态为空。
        head 和 tail 分别指向链表的头和尾节点。
        size 用于记录链表的长度。
        """
        self.head = None  # 链表头节点
        self.tail = None  # 链表尾节点
        self.size = 0  # 链表节点数

    def get(self, index: int) -> int:
        """
        获取链表中第 index 个节点的值。如果索引无效，则返回 -1。
        """
        if index < 0 or index >= self.size:  # 检查索引是否有效
            return -1
        
        # 优化查找方向：根据索引靠近头部还是尾部决定遍历方向
        if index < self.size // 2:
            current = self.head  # 从头部开始遍历
            for i in range(index):
                current = current.next
        else:
            current = self.tail  # 从尾部开始遍历
            for i in range(self.size - index - 1):
                current = current.prev
                
        return current.val  # 返回目标节点的值

    def addAtHead(self, val: int) -> None:
        """
        在链表头部插入一个值为 val 的节点。
        """
        new_node = ListNode(val, None, self.head)  # 创建新节点，指向原头节点
        if self.head:  # 如果链表非空，更新原头节点的 prev 指针
            self.head.prev = new_node
        else:  # 如果链表为空，新节点同时是头节点和尾节点
            self.tail = new_node
        self.head = new_node  # 更新头节点为新节点
        self.size += 1  # 增加链表大小

    def addAtTail(self, val: int) -> None:
        """
        在链表尾部插入一个值为 val 的节点。
        """
        new_node = ListNode(val, self.tail, None)  # 创建新节点，指向原尾节点
        if self.tail:  # 如果链表非空，更新原尾节点的 next 指针
            self.tail.next = new_node
        else:  # 如果链表为空，新节点同时是头节点和尾节点
            self.head = new_node
        self.tail = new_node  # 更新尾节点为新节点
        self.size += 1  # 增加链表大小

    def addAtIndex(self, index: int, val: int) -> None:
        """
        在链表中的第 index 个节点之前插入一个值为 val 的节点。
        如果 index 等于链表长度，则节点附加到链表末尾。
        如果 index 小于 0，则在头部插入节点。
        如果 index 大于链表长度，则不插入节点。
        """
        if index < 0:  # 如果索引小于 0，等同于在头部插入
            index = 0
        if index > self.size:  # 如果索引超出范围，不执行操作
            return
        
        if index == 0:  # 在头部插入
            self.addAtHead(val)
        elif index == self.size:  # 在尾部插入
            self.addAtTail(val)
        else:  # 在链表中间插入
            # 根据索引靠近头部还是尾部决定遍历方向
            if index < self.size // 2:
                current = self.head
                for i in range(index - 1):  # 找到目标位置的前一个节点
                    current = current.next
            else:
                current = self.tail
                for i in range(self.size - index):  # 找到目标位置的前一个节点
                    current = current.prev
            
            # 创建新节点并插入链表
            new_node = ListNode(val, current, current.next)
            current.next.prev = new_node
            current.next = new_node
            self.size += 1  # 增加链表大小

    def deleteAtIndex(self, index: int) -> None:
        """
        删除链表中第 index 个节点。如果索引无效则不执行操作。
        """
        if index < 0 or index >= self.size:  # 检查索引是否有效
            return
        
        if index == 0:  # 删除头节点
            self.head = self.head.next
            if self.head:  # 如果链表不为空，更新新头节点的 prev 指针
                self.head.prev = None
            else:  # 如果链表为空，同时更新尾节点
                self.tail = None
        elif index == self.size - 1:  # 删除尾节点
            self.tail = self.tail.prev
            if self.tail:  # 如果链表不为空，更新新尾节点的 next 指针
                self.tail.next = None
            else:  # 如果链表为空，同时更新头节点
                self.head = None
        else:  # 删除中间节点
            # 根据索引靠近头部还是尾部决定遍历方向
            if index < self.size // 2:
                current = self.head
                for i in range(index):  # 找到目标节点
                    current = current.next
            else:
                current = self.tail
                for i in range(self.size - index - 1):  # 找到目标节点
                    current = current.prev
            
            # 删除节点，更新前后指针
            current.prev.next = current.next
            current.next.prev = current.prev
        
        self.size -= 1  # 减少链表大小


# 使用示例
# 实例化链表
obj = MyLinkedList()
obj.addAtHead(1)       # 链表: 1
obj.addAtTail(3)       # 链表: 1 <-> 3
obj.addAtIndex(1, 2)   # 链表: 1 <-> 2 <-> 3
print(obj.get(1))      # 输出: 2
obj.deleteAtIndex(1)   # 链表: 1 <-> 3
print(obj.get(1))      # 输出: 3
