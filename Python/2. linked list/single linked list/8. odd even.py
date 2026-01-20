from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head                  # first node
        even = head.next            # second node
        even_head = even            # save start of even list

        while even and even.next:
            odd.next = even.next    # link odd nodes
            odd = odd.next

            even.next = odd.next    # link even nodes
            even = even.next

        odd.next = even_head        # attach even list at end
        return head

    
    def print_linked_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

example = Solution()
new_head = example.oddEvenList(head)
print(example.print_linked_list(new_head))
