// Function duplicateZeros(arr):
//     n = length of arr

//     For i from 0 to n-1:
//         If arr[i] == 0:
//             // Shift all elements to the right starting from the end
//             For j from n-2 down to i+1:
//                 arr[j+1] = arr[j]
            
//             // Duplicate the zero
//             arr[i+1] = 0

//             // Skip the next index because we just duplicated zero
//             i = i + 1


function duplicateZeros (arr) {
    let n = arr.length
    for(let i = 0; i < n; i++){
        if (arr[i] == 0){
            for(let j = arr[i]; j < n; j++){
                arr[j + 1] = arr[j]
                arr[i+1] = 0
                i = i+1
            }
        }
    }
}

duplicateZeros([1,0,2,3,0,4,5,0])