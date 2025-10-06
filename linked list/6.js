// Check if the node value equals to val

var removeElements = function(head, val) {
    let dummy = new ListNode(0, head); // dummy points to head
    let current = dummy;

    while (current.next !== null) {
        if (current.next.val === val) {
            current.next = current.next.next; // skip the node
        } else {
            current = current.next; // move forward
        }
    }

    return dummy.next; // return new head
};