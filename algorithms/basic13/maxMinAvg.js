var arr = [5, 6, -5, 12, 34, -22, 56, 90, -1, 18];
function maxMinAvg(arr){
  var max = arr[0];
  var min = arr[0];
  var sum = 0;
  for(i=0; i<arr.length; i+=1){
    sum += arr[i];
    if(arr[i] > max){
      max = arr[i]
    }
    else if (arr[i] < min) {
      min = arr[i];
    }
  }
  var avg = sum / arr.length;
  console.log(max, min, avg);
}
maxMinAvg(arr);
