// Create ThreesFives() that adds values from 100 and 4000000 (inclusive) if that value is evenly divisible by 3 or 5 but not both. Display the final sum in the console.
//
// Second: Create BetterThreesFives(start,end) that allows you to enter arbitrary start and end values for your range. Think of your above ThreesFives() function as BetterThreesFives(100,4000000).
function ThreesFives(num1, num2){
  var sum = 0;
  for(i=num1; i<= num2; i+=1){
    if(i%3==0 && i%5==0){
      sum += i
    }
  }
  console.log(sum);
}
ThreesFives(100, 4000000)
