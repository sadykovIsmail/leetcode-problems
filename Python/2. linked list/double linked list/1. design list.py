class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        current = self.head
        i = 0

        while i < index:
            if not current:
                return -1
            current = current.next
            i += 1

        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        value = ListNode(val)

        if not self.head:
            self.head = value
            return

        value.next = self.head
        self.head.prev = value
        self.head = value

    def addAtTail(self, val: int) -> None:
        value = ListNode(val)

        if not self.head:
            self.head = value
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = value
        value.prev = cur

    def addAtIndex(self, index: int, val: int) -> None:
        # ✅ minimal fix: prevent crash
        if index > 0 and not self.head:
            return

        if index <= 0:
            self.addAtHead(val)
            return

        value = ListNode(val)
        head = self.head
        i = 0

        while i < index - 1:
            if not head.next:
                self.addAtTail(val)
                return
            head = head.next
            i += 1

        value.next = head.next
        value.prev = head

        if head.next:
            head.next.prev = value

        head.next = value

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return

        head = self.head
        i = 0

        while i < index:
            if not head:
                return
            head = head.next
            i += 1

        if not head:
            return

        if head.prev:
            head.prev.next = head.next
        if head.next:
            head.next.prev = head.prev

    def print_linked_list(self):
        result = []
        head = self.head
        while head:
            result.append(head.val)
            head = head.next
        return result


# ===== TEST =====
example = MyLinkedList()
example.addAtHead(4)
example.addAtHead(2)
example.addAtHead(1)
example.addAtTail(5)
example.addAtIndex(2, 3)
example.deleteAtIndex(1)

print(example.print_linked_list())  # ✅ [1, 3, 4, 5]
