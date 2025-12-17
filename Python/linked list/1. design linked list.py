class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        current = self.head
        i = 0

        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1

        return -1


    def addAtHead(self, val: int) -> None:
        value = ListNode(val)
         
        current = self.head
        self.head = value
        value.next = current

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
    
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
def addAtIndex(self, index: int, val: int) -> None:
    if index <= 0:
        self.addAtHead(val)
        return

    i = 0
    current = self.head

    while current and i < index - 1:
        current = current.next
        i += 1

    if not current:
        return  # index > length → do nothing

    new_node = ListNode(val)
    new_node.next = current.next
    current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

ll = MyLinkedList()

node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
ll.head = node1
node1.next = node2
node2.next = node3

# adding 5 at tail
print(ll.get(0))
print(ll.get(2))  # should print 30
print(ll.get(3))  # should print 5
ll.addAtIndex(3, 8)
print(ll.get(3))
