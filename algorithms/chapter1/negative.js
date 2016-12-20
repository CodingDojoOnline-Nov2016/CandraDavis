// Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].
function negative(arr){
  for (var i = 0; i < arr.length; i += 1){
    if(arr[i] > 0){
      arr[i] = 0 - arr[i];
    }
  }
  return arr;
}
negative([3, 4, 5, -2, 1, -3, 6])
