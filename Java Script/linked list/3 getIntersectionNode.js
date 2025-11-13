/*
given two linked list, we meed to find the node where they meet 

PseudoCode:
funtion headA headB

arrA = []
arrB = []
while headA.next AND headB.next
if headA === headB 
return headA

if arrA.has headB return headB

if arrB.has headA return headA

headA = headA.next
headB = headB.next
arrA.push headB
arrB.push headA

after return 
null
*/

const getIntersectionNode = function(headA, headB) {
    if (!headA || !headB) return null;

    let visited = new Set();

    // Traverse the first list and add each node to the set
    let current = headA;
    while (current) {
        visited.add(current);
        current = current.next;
    }

    // Traverse the second list and check for intersection
    current = headB;
    while (current) {
        if (visited.has(current)) return current;
        current = current.next;
    }

    // No intersection found
    return null;
};

