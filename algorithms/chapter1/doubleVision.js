// Given array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.
function double(arr){
  var new_array = [];
  for (i = 0; i < arr.length; i += 1){
    new_array.push(arr[i]*2);
  }
  return new_array;
}
double([1,2,3]);
