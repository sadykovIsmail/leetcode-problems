// reverse so head becomes the last

var reverseList = function(head) {
    let newHead = null; // this will become the new head of the reversed list

    while (head !== null) {
        let nextNode = head.next; // store the next node
        head.next = newHead;      // move current node to the front
        newHead = head;           // update new head
        head = nextNode;          // move to the next node in original list
    }

    return newHead; // new head of reversed list
};
