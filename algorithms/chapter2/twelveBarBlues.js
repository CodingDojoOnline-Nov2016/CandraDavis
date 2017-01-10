// Write a function that console.logs the number 1, then "chick", then "boom", then "chick", then 2, then "chick", then "boom", then "chick" - continuing the same cycle for each number up to (including) 12.
function blues(num){
  var b = ' boom'
  var c = ' chick'
  for(i=1; i<= num; i++){
    console.log(i + c + b + c);
  }
}
blues(5);
