// Given an array and a value Y, count and print the number of array values greater than Y.
var arr = [5, 6, 12, 34, 56, 90, 18];
function greaterThanY(arr, y){
  var count = 0;
  for(i=0; i<arr.length; i+=1){
    if(arr[i] > y){
    count +=1;
    console.log(count, arr[i]);
    }
  }
}
greaterThanY(arr, 6);
