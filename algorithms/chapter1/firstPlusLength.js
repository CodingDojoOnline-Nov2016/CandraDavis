function firstPlusLength(arr){
  var addFirstAndLength = arr.length + arr[0];
  return addFirstAndLength;
}

firstPlusLength([5, 6, 7, 8, 9, 10, 12, 13, 15])
firstPlusLength(['3', 5, 19, 4]) //this returns a string of '43'
firstPlusLength([true, 6, 3, 7]) //this counts true = 1, then adds length of 4 to 1 to equal 5
