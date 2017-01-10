// Print integers from 0 to 255, and with each integer print the sum so far.
function printPlusSum255(){
  var sum = 0;
  for(i=0; i<=255; i+=1){
    console.log(i, sum + i);
    sum = sum + i
  }
}
printPlusSum255();
