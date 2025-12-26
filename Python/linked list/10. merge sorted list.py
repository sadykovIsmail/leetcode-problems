# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 or not list2:
            if not list1:
                return list2
            return list1
        
        
        dummy = ListNode(0)
        cur = dummy
        first = list1
        second = list2
        
        while first or second:
            if not first:
                cur.next = second
                return dummy.next
            elif not second:
                cur.next = first
                
                return dummy.next
            if first.val < second.val:
                cur.next = first
                first = first.next
                cur = cur.next
                
            else:
                cur.next = second
                second = second.next
                cur = cur.next
                
                
        return dummy.next
        
        
        
        
# Cleaner
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # attach the remaining list
        cur.next = list1 if list1 else list2

        return dummy.next

"""
