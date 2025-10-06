var oddEvenList = function(head) {
    // Edge case: if list is empty or has only one node, return as is
    if (!head || !head.next) return head;

    // Initialize pointers
    let odd = head;           // starts at the first node (position 1)
    let even = head.next;     // starts at the second node (position 2)
    let evenHead = even;      // keep the head of even nodes to attach later

    // Traverse the list
    while (even !== null && even.next !== null) {
        odd.next = even.next; // link current odd node to the next odd node
        odd = odd.next;       // move odd pointer forward

        even.next = odd.next; // link current even node to the next even node
        even = even.next;     // move even pointer forward
    }

    // Connect the last odd node to the head of even nodes
    odd.next = evenHead;

    // Return the head of the reordered list
    return head;
};
