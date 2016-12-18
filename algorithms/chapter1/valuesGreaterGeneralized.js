// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.
// Print how many values this is. What will you do if the array is only one element long?

function greaterThan2nd(arr){
  var new_array = [];
  for (i = 0; i < arr.length; i +=1){
      if (arr[i] > arr[1]) {
      new_array.push(arr[i]); // new_array.push(i) returns a new array with the index number of each val greater than arr[1]
    }
  }
  console.log(new_array);
  console.log(new_array.length);
}

greaterThan2nd([1,3,5,7,9,13]);
greaterThan2nd([5]); // 1 value returns an empty array and a length of 0
