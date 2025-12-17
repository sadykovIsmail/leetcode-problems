const detectCycle = function(head) {
    if(!head || !head.next){
        return null
    }

    let slow = head.next
    let fast = head.next.next

    while(fast && fast.next){
        slow = slow.next
        fast = fast.next.next
        if(fast == slow){
            let point1 = slow
            let point2 = head
            while(point1 !== point2){
                point1 =  point1.next
                point2 = point2.next
            }
            return point1
        }
    }
    return null
};

//DON'T FORGET TO MOVE POINTS LIKE: point = point.next 
