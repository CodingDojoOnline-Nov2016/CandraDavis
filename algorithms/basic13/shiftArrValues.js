// Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.
var arr = [5, 6, -5, 12, 34, -22, 56, 90, -1, 18];
function shiftArr(arr){
  for(i=0; i<arr.length-1; i+=1){
    arr[i] = arr[i+1];  
  }
  arr[arr.length-1] = 0;
  return arr;
}
shiftArr(arr);
