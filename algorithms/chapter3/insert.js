// Given an array, index, and additional value, insert the value into the array at given index. Do this without using built-in array methods. You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).
function insertAt(arr, indx, val){
  arr[indx] = val;
  return console.log(arr);
}
var x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];
insertAt(x, 5, 21);
