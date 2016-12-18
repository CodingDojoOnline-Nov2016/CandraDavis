// Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.
function print1RtnAnother(arr){
  console.log(arr[arr.length - 2]);
  for (i = 0; i < arr.length; i += 1){
    if( arr[i] % 2 != 0){
      return(arr[i]);
    }
  }
}
print1RtnAnother([2, 4, 6, 7, 12, 14, 19]);
