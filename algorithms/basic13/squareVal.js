// Square each value in a given array, returning that same array with changed values.
function squareVal(arr){
  for(i=0; i<arr.length; i+=1){
    arr[i] *= arr[i];
  }
  return arr;
}
squareVal([5, 6, 12, 34, 56, 90, 18]);
