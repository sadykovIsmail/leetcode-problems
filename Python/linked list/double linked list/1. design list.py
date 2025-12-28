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
        current = self.head

        if index < 1:
            # current.next = None
            return current.val
        i = 0
        
        while i < index:
            if not current:
                return None
            current = current.next
            i += 1
            
            
        
        
            
        return current.val
        

    def addAtHead(self, val: int) -> None:
        
        value = ListNode(val)
        
        if not self.head:
            self.head = value
            return
            
        head = self.head
        
        value.next = head
        head.prev = value
        self.head = value
        return

    def addAtTail(self, val: int) -> None:
        value = ListNode(val)
        
        cur = self.head
        if not self.head:
            self.head = value
            return
        
        while cur.next:
            cur = cur.next
        value.next = None
        value.prev = cur
        cur.next = value
        return 

    def addAtIndex(self, index: int, val: int) -> None:
        value = ListNode(val)
        head = self.head
        if index <= 0:
            self.addAtHead(val)
            return
        i = 0
        
        while i < index:
            if not head.next:
                self.addAtTail(val)
                return
            head = head.next
            i += 1
        value.next = head
        value.prev = head.prev
        head.prev.next = value
        head.prev = value
        return
            
        
            

    # def deleteAtIndex(self, index: int) -> None:
        
        
    def print_linked_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result


example = MyLinkedList()
param_4 = example.addAtHead(4)
param_2 = example.addAtHead(2)
param_1 = example.addAtHead(1)
param_5 = example.addAtTail(5)
param_3 = example.addAtIndex(2, 3)



# get = example.get(1)
# print(get)
print(example.print_linked_list(param_3))
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)