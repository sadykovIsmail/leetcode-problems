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