// Stan learned something today: that reducing an array’s .length immediately shortens it by that amount. Given array arr and number X, remove all except the last X elements, and return arr (changed and shorter). Given ([2,4,6,8,10],3), change the given array to [6,8,10] and return it.
function reduceArr(arr, x){
  var temp = []
  for(var i = arr.length - x; i < arr.length; i += 1){
    temp.push(arr[i]);
  }
  var arr = temp;
  return arr;
}
reduceArr([2,4,6,8,10], 3)
