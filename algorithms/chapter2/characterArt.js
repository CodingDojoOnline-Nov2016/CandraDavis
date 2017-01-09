// From Star Art, derive the following that will accept and draw the given characters, not just asterisks:
//
// For all three of these, you can safely assume that 'char' is a string with length 1.

// drawLeftChars(num, char)
function drawLeftChars(num, char){
  var textField = ''
  for(i=0; i<=75; i++)
    if(num>0){
      textField += char
      num -=1
    }
    else{
      textField += ' '
    }
  console.log(textField);
}
drawLeftChars(25, 'c')
// drawRightChars(num, char)
function drawRightChars(num, char){
  var textField = '';
  var blanks = 75 - num;
  for(i=0; i<=75; i+=1){
    if(blanks>0){
      textField += ' '
      blanks -=1;
    }
    else{
      textField += char;
    }
  }
  console.log(textField);
}
drawRightChars(35, 'G');

// drawCenterChar(num, char)
function drawCenterChar(num, char){
  var textField = ''
  var spaces = (75-num)/2
  for(i=0; i<=75; i+=1){
    if(spaces>0){
      textField += ' '
      spaces -=1
    }
    else if (num>0) {
      textField += char
      num -=1
    }
    else{
      textField += ' '
    }
  }
  console.log(textField);
}
drawCenterChar(21, 'a')
