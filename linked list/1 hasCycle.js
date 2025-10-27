const hasCycle = function (head) {
    if(!head || !head.next){
        return false
    }
let slow = head.next
let fast = head.next.next

while(fast && fast.next){

    if(fast === slow){
        return true
    }
    slow = slow.next
    fast = fast.next.next
}
return false
}