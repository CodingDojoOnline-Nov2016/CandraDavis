function whatHappensToday(num){
  var kenny = 'Kenny died today in a ';

  if (num <= .10){
    console.log(kenny + 'volcanoe');
  }
  else if (num >.10 &&  num<= .15) {
    console.log(kenny + 'tsunami');
  }
  else if (num > .15 && num <= .20) {
    console.log(kenny + 'earthquake');
  }
  else if (num > .20 && num <= .25) {
    console.log(kenny + 'blizzard');
  }
  else if (num > .25 && num <= .30) {
    console.log(kenny + 'meteor strike');
  }
  else(console.log('Kenny lives!'));
}
var randNum = Math.random();
var probability = randNum.toFixed(2);
whatHappensToday(probability);
