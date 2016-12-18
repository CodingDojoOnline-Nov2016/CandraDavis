// Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.
function thisThat(num1, num2) {
  var arr = [];
    while (num1 >= arr.length){
      arr.push(num2);
    }
    console.log(arr);
    if (num1 === num2) {
      console.log('Jinx!');
    }
}

thisThat(12, 5);
thisThat(3, 3)
