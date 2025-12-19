# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None
        head_node = head
        currentA = head_node
        i = 1
        j = 1
        while currentA.next:
            currentA = currentA.next
            i += 1
            
        point = i - n
        if point == 0:
            return head_node.next
        currentB = head
        while j < point:
            j += 1
            currentB = currentB.next
        currentB.next = currentB.next.next
        return head_node
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
n = 2

test = Solution()

print(test.removeNthFromEnd(head, n))
