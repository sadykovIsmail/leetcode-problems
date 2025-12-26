# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        head = head
        
        while head:
            values.append(head.val)
            head = head.next
            
        left = 0
        right = len(values) - 1
        
        while left < right:
            if values[left] != values[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
        
            
        
    
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

example = Solution()
print(example.isPalindrome(head))



# How should be
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1️⃣ Find middle (slow ends at mid)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # 3️⃣ Compare both halves
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
