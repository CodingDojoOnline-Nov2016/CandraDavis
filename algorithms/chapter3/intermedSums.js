// You will be given an array of numbers. After every tenth element, add an additional element containing the sum of those ten values. If the array does not end aligned evenly with ten elements, add one last sum that includes those last elements not yet been included in one of the earlier sums. Given the array [1,2,1,2,1,2,1,2,1,2,1,2,1,2], change it to [1,2,1,2,1,2,1,2,1,2,15,1,2,1,2,6].

function intermediateSums(arr){
  var count = 0;
  var sum = 0;
  var sumArr = [];
  for(var i = 0; i < arr.length; i += 1){
    sum += arr[i];
    sumArr.push(arr[i]);
    count += 1;
    if(count % 10 === 0){
      sumArr.push(sum);
      sum = 0;
      var lengthOf10s = arr.length % 10;
      if(lengthOf10s !== 0){
        for(var j = arr.length - lengthOf10s; j > 0; j += 1){
          sum += j;
        }
        sumArr.push(sum);
      }
    }
  }
  return console.log(arr);
}
intermediateSums([1,2,1,2,1,2,1,2,1,2,1,2,1,2]);
