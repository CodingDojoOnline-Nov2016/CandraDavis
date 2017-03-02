// Alan is good at breaking secret codes. One tool is to eliminate numbers he knows are outside a certain specific range. Given arr and values min and max, remove array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.

function filterRange(arr, min, max){
  console.log(arr.length);
  var diff = max - min;
  for(var i = min + 1; i < min + diff && i < arr.length - 1; i++){
    arr[i] = arr[i + diff];
    // if (arr[i + diff] < arr.length - 1){
    //   break;
    }
  var remove = diff - 1;
  arr.length -= remove;
  return console.log(arr);
}
var x = [ 1, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24];

filterRange(x, 3, 8);
