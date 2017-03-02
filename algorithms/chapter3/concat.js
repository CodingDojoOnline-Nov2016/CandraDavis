// Replicate JavaScript’s concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array’s elements, followed by the second array’s elements. Do not alter the original arrays.
//
// Example: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2]

function concat(arr1, arr2){
  for(var i = 0; i < arr2.length; i += 1){
    arr1.push(arr2[i]);
  }
  return console.log(arr1);
}

concat([1, 2, 3, 4], [5, 6, 7, 8])
