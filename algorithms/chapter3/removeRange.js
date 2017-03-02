// Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array). Given ([20,30,40,50,60,70],2,4), change to [20,30,70] and return it.

function removeRange(arr, min, max){
  var remove = (max - min) + 1;
  for(var i = min; i < arr.length; i++){
    arr[i] = arr[i + remove];
    // if (arr[i + diff] < arr.length - 1){
    //   break;
    }
  arr.length -= remove;
  return console.log(arr);
}

removeRange([20,30,40,50,60,70],2,4);
