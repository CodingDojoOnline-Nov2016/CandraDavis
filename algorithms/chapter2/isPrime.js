// Is Prime
// Return whether a given integer is prime. Prime numbers are only evenly divisible by themselves and 1. Many highly optimized solutions exist, however for now, just create one that is easy to understand and debug.
function isPrime(num){
  var count = 0
  for(i=1; i<=num; i+=1){
    if(num%i == 0){
      count +=1
    }
  }
    if(count == 2){
      console.log(num + ' is prime');
    }
    else{
      console.log(num + ' is not prime');
    }
}
isPrime(17);
isPrime(32);
