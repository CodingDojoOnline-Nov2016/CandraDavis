function mostSigDig(num){
  if (num < 0){
    // changes number to a positive value, then goes into the else statement
    num = Math.abs(num);
    console.log(num, 'negative number');
   }
   // if the number is a decimal, multiply the number until you get it greater than 0, then goes into else statement.
  if ((num < 1) && (num > 0)){
    while (Math.floor(num) === 0){
      num *= 10;
      console.log(num, 'moving number to the left to get to ones place...');
     }
   }
  else {
    // if the number is greater than 0, divide it by 10 until you get 1st digit to the 10ths place.
    while (Math.floor(num) > 0){
      num = num / 10;
      console.log(num, 'getting the first value');
    }
    // once the first digit is in the 10ths place, multiply by 10 to bring it to the 1s place.
    num *= 10;
    console.log(num, 'how has number changed?');
  }
  // this divides off any trailing decimal places and returns the first digit.
  num = Math.floor(num % 10);
  return console.log(num)
}

mostSigDig(0.007234);
mostSigDig(123456);
mostSigDig(-5467.295);
