// Swap positions of successive pairs of values of given array. If the length is odd, do not change the final element. For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. As with all array challenges, do this without using any built-in array methods.

function swapPairs(arr){
  var temp,
      x;
  for(var i =0; i < arr.length - 1; i += 1){
    if(i % 2 === 0){
      temp = arr[i];
      x = arr[i + 1];
      arr[i] = x;
      arr[i + 1] = temp;
    }
  }
  return console.log(arr);
}
var y = [1, 2, 3, 4];
var w = ['blast', 2, 'huge']
swapPairs(y);
swapPairs(w);
