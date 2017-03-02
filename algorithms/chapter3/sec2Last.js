// Return the second-to-last element of an array. Given [42,true,4,"Liam",7], return "Liam". If the array is too short, return null.

function sec2Last(arr){
  var secondToLast = arr[arr.length - 2]
  if(secondToLast < 0){
    secondToLast = null;
  }
  return console.log(secondToLast);
}
sec2Last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
