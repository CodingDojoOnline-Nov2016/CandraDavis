// Return the given array, after setting any negative values to zero.
var arr = [5, 6, -5, 12, 34, -22, 56, 90, -1, 18];
function zero4NegNum(arr){
  for(i=0; i<arr.length; i+=1){
    if(arr[i]<0){
      arr[i] = 0;
    }
  }
  return arr;
}
zero4NegNum(arr);
