// Values Greater than Second
// For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

function greaterThan2nd(arr){
  for (i = 0; i < arr.length; i +=1){
      if (arr[i] > arr[1]) {
      console.log(arr[i]);
    }
  }
}

greaterThan2nd([1,3,5,7,9,13]);
