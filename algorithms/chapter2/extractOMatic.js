// Create the extractDigit(num,digitNum) function that given a number and a digit number, returns the numeral value of that digit. 0 represents the ones digit, 1 represents the tens digit, etc. Given (1824,2), return 8. Given (1824,0), return 4. Given (1824,7), return 0.
//
// Second: handle negative digitNum values, where -1 represents tenths digit (0.x), -2 represents hundredths digit (0.0x), etc. Given (123.45,-1), return 4.
//
// Third: handle negative num values as well, doing what you think is appropriate.
//

function extractDigit(num, digitNum){
  var stringNum = num.toString();
  console.log(stringNum);
  console.log(stringNum.length);
  for(var i = stringNum.length - 1; i>=0; i-= 1){
    if(digitNum === i){
      return console.log(stringNum[i])
    }
    else{
      continue;
    }
  }
}
extractDigit(1824,0);
