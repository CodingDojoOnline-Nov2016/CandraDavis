// Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"

function evenOdds(arr){
  var count = 0;
  for (i = 0; i < arr.length; i +=1){
    if (arr[i]%2 == 1){
      count +=1;
      if (count / 3 == 1){
        console.log("That's Odd!");
      }
      else if (count / 3 >= 2) {
        console.log("Even more so!");
      }
    }
  }
}
evenOdds([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 4]);
