class ListNode {
    constructor (val, next){
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
    }

}
// Given head = [1,2,3,4,5]
const reverseList = function(head) {
  let prev = null
  let curr = head

  while (curr !== null) {
    let nextNode = curr.next   // store next node
    curr.next = prev           // reverse pointer
    prev = curr                // move prev forward
    curr = nextNode            // move curr forward
  }

  return prev
}
