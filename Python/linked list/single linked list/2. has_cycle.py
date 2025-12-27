# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        
        slow = head.next
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        return False
        