class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self, head):
        self.head = head
        

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
            i += 1
        current.next = None
        return current

    def addAtHead(self, val: int) -> None:
        
        value = ListNode(val)
        
        if not self.head:
            self.head = value
            
        head = self.head
        
        value.next = head
        head.prev = value
        return value

    # def addAtTail(self, val: int) -> None:
        

    # def addAtIndex(self, index: int, val: int) -> None:
        

    # def deleteAtIndex(self, index: int) -> None:
        
        
    def print_linked_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

node4.prev = node3
node3.prev = node2
node2.prev = node1
node1.prev = None

head = node1


example = MyLinkedList(head)
param_1 = example.get(2)
print(example.print_linked_list(param_1))
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)