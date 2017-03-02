// Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().

function skyline(arr){
  var max = arr[0];
  var min = arr[0];
  var arr2 = [];
  for(var i = 0; i < arr.length; i += 1){
    if (arr[i] < min && arr[i] > 0){
      min = arr[i]
    }
    else if(arr[i] > max){
      
    }
  }
}
