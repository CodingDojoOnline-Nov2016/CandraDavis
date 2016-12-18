function countdown(num){
  var count_array = [];
  var i = num
  while (i >= 0){
    count_array.push(i);
    i--;
  }
  console.log(count_array);
}
countdown(10);
