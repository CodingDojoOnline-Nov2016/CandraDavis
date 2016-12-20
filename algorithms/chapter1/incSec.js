// Given an array of numbers arr, add 1 to every second element, specifically those whose index is odd (arr[1], [3], [5], etc). Afterward, console.log each array value and return arr.
function incSec(arr){
  for (i=0; i < arr.length; i +=1){
    if (i % 2 === 1){
      arr[i] +=1;
      console.log(arr[i]);
    }
  }
  return arr;
}
incSec([3, 5, 1, 3, 5, 9, 7, 19, 23, 25, 10, 11, 2, 6]);
