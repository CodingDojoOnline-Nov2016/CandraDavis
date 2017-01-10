// Given an array, find and print its largest element.
var arr = [5, 6, 12, 34, 56, 90, 18];
var max = arr[0];
for(i=0; i<arr.length; i+=1){
  if(arr[i] > max){
    max = arr[i]
  }
}
console.log(max);
