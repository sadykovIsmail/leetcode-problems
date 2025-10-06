let head = new ListNode(6, new ListNode(15));
let newNode = new ListNode(9);

// Insert 9 after 6
insertAfter(head, newNode);

// Resulting list: 6 -> 9 -> 15

// Insert at beginning
head = insertAtBeginning(head, new ListNode(3));
// List: 3 -> 6 -> 9 -> 15

// Insert at end
head = insertAtEnd(head, new ListNode(20));
// List: 3 -> 6 -> 9 -> 15 -> 20
