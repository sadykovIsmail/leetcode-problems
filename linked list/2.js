// find where cycle starts

var detectCycle = function(head) {
    if (!head || !head.next) return null;

    let slow = head;
    let fast = head;

    // Step 1: Detect cycle
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;

        if (slow === fast) {
            // Step 2: Find start of cycle
            let ptr1 = head;
            let ptr2 = slow;
            while (ptr1 !== ptr2) {
                ptr1 = ptr1.next;
                ptr2 = ptr2.next;
            }
            return ptr1; // cycle start
        }
    }

    return null; // no cycle
};
