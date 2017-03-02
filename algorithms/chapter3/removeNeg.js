// Implement removeNegatives() function that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order. As always, do not use built-in array functions.

function removeNegatives(arr){
  for(var i = 0; i < arr.length; i += 1){
    if(arr[i] < 0){
      arr[i] = arr[i + 1];
    }
  }
  for(var j = arr.length - 1; j > 0; i -= 1){
    if(arr[i] === arr[i - 1]){
      
    }
  }
  return console.log(arr);
}

var x = [-1, 4, -3, 5, -7, 2];
removeNegatives(x); // expecting [4, 5, 2]
// Second: don’t use nested loops.
