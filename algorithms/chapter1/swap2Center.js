// Given array, swap first and last, third and third-tolast, etc. Input[true,42,"Ada",2,"pizza"] becomes ["pizza",42,"Ada",2,true]. Change [1,2,3,4,5,6] to [6,2,4,3,5,1].
function swap2Center(arr){
  var x = 1;
  var y = arr.length;
    while(x < y){
      var temp = arr[x];
      arr[x] = arr[y - 2];
      arr[y - 2] = temp;
      x += 2;
      y -= 2;
    }
    return arr;
  }
swap2Center([true,42,"Ada",2,"pizza"]);
swap2Center([1,2,3,4,5,6]);
