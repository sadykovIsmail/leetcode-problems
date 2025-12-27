# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        
        if not headA or not headB or not headA.next or not headB.next:
            return None
        currentA = headA
        
        while currentA:
            seen.add(currentA)
            currentA = currentA.next
            
        currentB = headB
        
        while currentB:
            if currentB in seen:
                return currentB.val
            seen.add(currentB)
            currentB = currentB.next
            
        return None
    
node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)

node_b_1 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

node_b_1.next = node3


test = Solution()

print(test.getIntersectionNode(node1, node_b_1))