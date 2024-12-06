class Node:
    """
    定义链表节点类。
    """
    def __init__(self, val=0, next=None):
        self.val = val  # 节点值
        self.next = next  # 下一个节点的指针


class MyLinkedList:
    """
    定义链表类，实现题目所要求的操作。
    """
    def __init__(self):
        self.head = None  # 初始化链表头指针
        self.size = 0  # 初始化链表的大小为0

    def get(self, index: int) -> int:
        """
        获取链表中第 index 个节点的值。如果索引无效，返回 -1。
        """
        if index < 0 or index >= self.size:  # 检查索引是否合法
            return -1
        
        current = self.head
        for _ in range(index):  # 遍历链表，找到目标节点
            current = current.next
        
        return current.val  # 返回目标节点的值

    def addAtHead(self, val: int):
        """
        在链表的第一个元素之前添加一个值为 val 的节点。
        """
        new_node = Node(val, self.head)  # 创建新节点，新节点指向当前头节点
        self.head = new_node  # 更新头节点为新节点
        self.size += 1  # 链表大小加1

    def addAtTail(self, val: int):
        """
        将值为 val 的节点追加到链表的最后一个元素。
        """
        new_node = Node(val)  # 创建新节点
        if not self.head:  # 如果链表为空，则新节点成为头节点
            self.head = new_node
        else:
            current = self.head
            while current.next:  # 遍历到链表的最后一个节点
                current = current.next
            current.next = new_node  # 将最后一个节点的 next 指向新节点
        
        self.size += 1  # 链表大小加1

    def addAtIndex(self, index: int, val: int):
        """
        在链表中的第 index 个节点之前添加值为 val 的节点。
        如果 index == 链表长度，则该节点将附加到链表末尾。
        如果 index 大于链表长度，则不会插入节点。
        如果 index 小于0，则在头部插入节点。
        """
        if index > self.size:  # 如果索引大于链表长度，不插入
            return
        if index <= 0:  # 如果索引小于等于0，在头部插入
            self.addAtHead(val)
            return
        if index == self.size:  # 如果索引等于链表长度，在尾部插入
            self.addAtTail(val)
            return

        # 在链表中间插入
        new_node = Node(val)
        current = self.head
        for _ in range(index - 1):  # 遍历到要插入位置的前一个节点
            current = current.next
        new_node.next = current.next  # 新节点指向目标位置的节点
        current.next = new_node  # 前一个节点指向新节点
        self.size += 1  # 链表大小加1

    def deleteAtIndex(self, index: int):
        """
        如果索引 index 有效，删除链表中的第 index 个节点。
        """
        if index < 0 or index >= self.size:  # 检查索引是否合法
            return
        if index == 0:  # 删除头节点
            self.head = self.head.next  # 更新头节点为下一个节点
        else:
            current = self.head
            for _ in range(index - 1):  # 遍历到要删除节点的前一个节点
                current = current.next
            current.next = current.next.next  # 跳过目标节点
        
        self.size -= 1  # 链表大小减1
