// remove nth element from node

var removeNthFromEnd = function(head, n) {
    let dummy = new ListNode(0)
    dummy.next = head
    
    let fast = dummy
    let slow = dummy
    let i = 0
    
    while(fast != null){
        if(i == n + 1){
            slow = slow.next
            fast = fast.next
        }else{
            fast = fast.next
            i++
        }
    }
    slow.next = slow.next.next 
    return dummy.next
    
    
};