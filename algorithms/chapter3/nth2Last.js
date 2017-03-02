// Return the element that is N-from-array’s-end. Given ([5,2,3,6,4,9,7],3), return 4. If the array is too short, return null.
function nth2Last(arr, val){
  var nthToLast = arr[arr.length - val];
  if(nthToLast < 0){
    nthToLast = null;
  }
  return console.log(nthToLast);
}
nth2Last([5,2,3,6,4,9,7],3);
