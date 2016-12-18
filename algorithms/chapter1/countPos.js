// Given array of numbers, create function to replace last value with number of positive values.
// Example: countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.

function countPositives(arr){
  var count = 0;
  for (i = 0; i < arr.length; i += 1){
    if (arr[i] > 0){
      count += 1;
    }
  }
  arr[arr.length-1] = count;
  return arr;
}
countPositives([-1,1,1,1]);
