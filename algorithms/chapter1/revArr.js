// Given array, write a function that reverses values, in-place.
// Example: reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].
function reverse(arr){
  var first = 0;
  var last = arr.length;
    while(first < last){
      var temp = arr[first];
      arr[first] = arr[last - 1];
      arr[last - 1] = temp;
      first += 1;
      last -= 1;
    }
    return arr;
  }
reverse([3,1,6,4,2]);
