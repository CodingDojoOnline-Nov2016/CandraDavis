// The Luhn formula is sometimes used to validate credit card numbers. Create the function isCreditCardValid(digitArr) that accepts an array of digits on the card (13-19 depending on the card), and returns a boolean whether the card digits satisfy the Luhn formula, as follows:
//
function isCreditCardValid(digitArr){
  // Set aside the last digit and do not include it in these calculations (until step 5);
  if(digitArr.length >= 13 && digitArr.length <= 19){
    var lastDig = digitArr.pop();
    console.log(lastDig);
    var sum = 0;
    // Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
    for(var i = digitArr.length - 1; i >= 0; i -= 1){
      console.log(i, 'index number');
      if(i % 2 !== 0){
        digitArr[i] *= 2;
        console.log(digitArr[i], 'multiplied by 2');
        // If any results are larger than 9, subtract 9 from them;
        if(digitArr[i] > 9){
          digitArr[i] -= 9;
          console.log(digitArr[i], 'subtracted 9');
        }
      }
      // Add all numbers (not just our odds) together;
      sum += digitArr[i];
      console.log(sum);
    }
    sum += lastDig;
    console.log(sum);
    // Now add the last digit back in – the sum should be a multiple of 10.
    if(sum % 10 !== 0){
      var isLuhn = false;
    }
    else{
      var isLuhn = true;
    }
  }
  return console.log(sum, isLuhn);
}
// For example, when given digit array [5,2,2,8,2], after step 1) is becomes [5,2,2,8], then after step 2) it is [5,4,2,16]. Post-step 3) we have [5,4,2,7], then following step 4) it becomes 18. After step 5) our value is 20, so ultimately we return true. If the final digit were any non-multiple-of-10, we would instead return false.
var creditCard = [3, 4, 5, 1, 6, 1, 3, 1, 9, 4, 8, 5, 3, 9, 7, 8];
var creditCard2 = [3, 4, 5, 1, 6, 1, 3, 1, 9, 4, 8, 5, 3, 9, 7, 4];
isCreditCardValid(creditCard);
isCreditCardValid(creditCard2);
