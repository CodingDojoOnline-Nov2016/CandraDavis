// Analyze an array’s values and print the average.
function getAndPrintAv(arr){
  var sum = 0;
  for(i=0; i<arr.lenth; i++){
    sum += arr[i];
  }
  var avg = sum/arr.length;
  return avg;
}
getAndPrintAv([5, 6, 12, 34, 56, 90, 18]);
