const oddEvenList = function(head) {
    if (!head) return null

    let odd = head
    let even = head.next
    let evenHead = even   // ✅ save start of even list

    while (even && even.next) {   // ✅ use AND instead of OR
        odd.next = even.next
        odd = odd.next            // ✅ move odd pointer

        even.next = odd.next
        even = even.next          // ✅ move even pointer
    }

    odd.next = evenHead           // ✅ connect odd list to even list
    return head                   // ✅ return original head, not odd
};
