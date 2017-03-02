// Given an array and an index into array, remove and return the array value at that index. Do this without using built-in array methods except for the pop(). Think of PopFront(arr) as equivalent to RemoveAt(arr,0).
function removeAt(arr, idx){
  var removed = arr.splice(idx, 1);
  return console.log(removed);
}
var x = [12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25];
removeAt(x, 4);
