// Sara is looking to hire an awesome web developer and has received applications from various sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. As with all these array challenges, do this without using any built-in array methods.
//
// Second: solve this without using any nested loops.

function removeDuplicate(arr){
  for(var i = 0; i < arr.length; i += 1){
    if(arr[i] === arr[i - 1]){
      arr.splice(i, 1)
    }
  }
  return console.log(arr);
}
var x = [12, 13, 14, 14, 15, 16, 16, 17, 18, 19, 20, 21, 21, 22, 22];

removeDuplicate(x);
