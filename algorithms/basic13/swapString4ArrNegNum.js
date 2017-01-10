var arr = [5, 6, -5, 12, 34, -22, 56, 90, -1, 18];
function swapString4Neg(arr){
  for(i=0; i<arr.length; i+=1){
    if(arr[i]<0){
      arr[i] = 'Dojo';
    }
  }
  return arr;
}
swapString4Neg(arr);
