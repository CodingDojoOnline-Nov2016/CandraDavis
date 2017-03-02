// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working ‘in-place’ means that you cannot use a second array – move values within the array that you are given. As always, do not use built-in array functions such as splice().
function reverse(arr){
  var temp = 0;
  var count = 0;
  for(var i = arr.length - 1; i >= arr.length / 2; i -= 1){
    temp = arr[i];
    arr[i] = arr[count];
    arr[count] = temp;
    count += 1;

    console.log(arr);
  }
  return console.log(arr);
}
reverse([3, 6, 8, 9, 11, 21, 4, 36])
