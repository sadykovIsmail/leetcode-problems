from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        i = 0
        current = head
        before = ListNode(0, current)
        count = 0
        
        
            
        
        while current:
            
            if current.val == val and i == 0:
                head = current.next
                i += 1
            if current.val == val and i != 0:
                before.next = before.next.next
                
            current = current.next
            before = before.next
            i += 1
        return head
    
    
node1 = ListNode(0)
node2 = ListNode(0)
node3 = ListNode(0)
node4 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
example = Solution()
print(example.removeElements(head, 0))
                
        