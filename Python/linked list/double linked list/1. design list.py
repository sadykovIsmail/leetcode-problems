class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        if not self.head:
            return None
        if index < 1:
            return self.head
        i = 0
        current = self.head
        while i < index:
            if not current:
                return None
            current = current.next
        return current

    # def addAtHead(self, val: int) -> None:
        

    # def addAtTail(self, val: int) -> None:
        

    # def addAtIndex(self, index: int, val: int) -> None:
        

    # def deleteAtIndex(self, index: int) -> None:
        

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

obj = MyLinkedList()
param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)