from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val == val:
                # delete the node
                current.next = current.next.next
            else:
                current = current.next  # only move if not deleted
        
        return dummy.next

# Helper to print linked list as Python list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test
node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(2)
node4 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
example = Solution()
new_head = example.removeElements(head, 0)
print(print_linked_list(new_head))
