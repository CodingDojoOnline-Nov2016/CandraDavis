// Create a function that takes array of numbers. The function should print the lowest value in the array, and return the highest value in the array.

function printLowRtnHigh(arr){
  var min = arr[0];
  var max = arr[0];
  for (i = 1; i < arr.length; i +=1){
    if (arr[i] < min){
      min = arr[i];
    }
    else if (arr[i] > max) {
      max = arr[i];
    }
  }
  console.log(min);
  return max;
}

printLowRtnHigh([-20, 5, 6, 19, 120, 75, 2000, -333, -555, 200]);
