class Node {
    constructor(val){
        this.val = val;
        this.next = null
    }
}



var MyLinkedList = function() {
    this.head = null
    this.size = 0
};

/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    if (index < 0 || index >= this.size) return -1;

    let current = this.head;
    for (let i = 0; i < index; i++) {
        current = current.next;
    }

    return current.val;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    let node = new Node(val)
    node.next = this.head
    this.head = node
    this.size++
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    let cur = new Node(val)

    if(!this.head){
        this.head = cur
    }else{
    let last = this.head
    while(last.next !== null){
        last = last.next
    }
    last.next = cur
    }
    
    
    this.size++

};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    if(index <= 0){
        this.addAtHead(val)
        return
    }
    else if(index === this.size){
        this.addAtTail(val)
        return
    }
    let head = this.head
    for(let i = 0; i < index - 1; i++){
        head = head.next
    }
    

    let cur = new Node(val)
    cur.next = head.next
    head.next = cur
    this.size++
};

/* 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if (index < 0 || index >= this.size) return;

    if (index === 0) {
        this.head = this.head.next;
    } else {
        let prev = this.head;
        for (let i = 0; i < index - 1; i++) {
            prev = prev.next;
        }
        prev.next = prev.next.next;
    }

    this.size--;
};


var obj = new MyLinkedList()
var param_1 = obj.get(index)
obj.addAtHead(val)
obj.addAtTail(val)
obj.addAtIndex(index,val)
obj.deleteAtIndex(index)
