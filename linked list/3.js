var getIntersectionNode = function(headA, headB) {
    if (!headA || !headB) return null;

    let pA = headA;
    let pB = headB;

    while (pA !== pB) {
        pA = pA ? pA.next : headB;
        pB = pB ? pB.next : headA;
    }

    return pA; // either intersection node or null
};
// where they meet together