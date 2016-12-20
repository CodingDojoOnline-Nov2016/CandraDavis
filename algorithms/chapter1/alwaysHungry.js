// Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". If no array elements are "food", then print "I'm hungry" once.
function hungry(arr){
  for(var i = 0; i < arr.length; i += 1){
    var count = 0;
    if (arr[i] === 'food'){
      console.log('yummy');
      count++;
      }
  }
  if(count === 0){
    console.log("I'm hungry");
  }
}
hungry(['food', 'food', 3, 4, 5, 6, 'food', 2, 'food']);
