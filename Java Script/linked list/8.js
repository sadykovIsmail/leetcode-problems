var isPalindrome = function(head) {
    let values = [];
    let current = head;

    // Step 1: store all node values in an array
    while (current !== null) {
        values.push(current.val);
        current = current.next;
    }

    // Step 2: check palindrome using two pointers
    let left = 0;
    let right = values.length - 1;
    while (left < right) {
        if (values[left] !== values[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
};
