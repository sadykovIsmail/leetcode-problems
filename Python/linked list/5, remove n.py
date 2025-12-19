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
        
        currentA = head
        i = 0
        j = 0
        while currentA.next:
            currentA = currentA.next
            i += 1
            
        point = i - n
        if point == 0:
            head = head.next
        currentB = head
        while j < point:
            j += 1
            currentB = currentB.next
        currentB.next = currentB.next.next
        return head