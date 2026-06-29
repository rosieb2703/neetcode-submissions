class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[ListNode] = None

class LinkedList:
    
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length or self.head is None:
            return -1

        current_node = self.head
        for _ in range(index):
            if current_node.next is None:
                return -1
            current_node = current_node.next

        return current_node.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length or self.head is None:
            return False

        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            removed_node.next = None
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next

            removed_node = prev_node.next
            prev_node.next = removed_node.next
            if removed_node == self.tail:
                self.tail = prev_node
            removed_node.next = None

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        array = []
        current_node = self.head
        while current_node:
            array.append(current_node.val)
            current_node = current_node.next
        return array