// Given an array of comparable values, move the lowest element to array’s front, shifting backward any elements previously ahead of it. Do not otherwise change the array’s order. Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. As always, do this without using built-in functions.
function min2Front(arr){
  var min = arr[0];
  var minIdx = 0;
  for(var i = 0; i < arr.length; i += 1){
    if(arr[i] < min){
      min = arr[i];
      minIdx = i;
    }
  }
  for(var j = minIdx; j > 0; j -= 1){
    arr[i] = arr[i - 1];
  }
  arr[0] = min;
  return console.log(arr);
}
var z = [4,2,1,3,5];

min2Front(z);
