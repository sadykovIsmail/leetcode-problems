class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        ll1 = l1
        ll2 = l2

        # append values, not nodes
        while ll1:
            list1.append(str(ll1.val))
            ll1 = ll1.next

        while ll2:
            list2.append(str(ll2.val))
            ll2 = ll2.next

        # reverse digits because input is in reverse order
        list1.reverse()
        list2.reverse()

        # sum as integer
        total = int("".join(list1)) + int("".join(list2))

        # build result linked list in reverse order
        dummy = ListNode(0)
        cur = dummy

        for digit in str(total)[::-1]:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return dummy.next  # must