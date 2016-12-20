// Build function that accepts array. Return a new array with all values except first, adding 7 to each. Do not alter the original array.
function add7ToMost(arr){
  var newArray = []
  for (var i = 1; i < arr.length; i++){
      newArray.push(arr[i] + 7);
  }
  return newArray;
}
var arr = [3, 4, 5, 6, 7, 8, 9, 10];
add7ToMost(arr);
