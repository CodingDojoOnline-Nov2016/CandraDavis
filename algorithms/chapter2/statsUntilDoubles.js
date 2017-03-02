// Here’s another game for our New Year’s Eve party. Implement a ’20-sided die’ that randomly returns integers between 1 and 20 inclusive. Roll these, tracking statistics until you get a value twice in a row. Display number of rolls, min, max, and average.

function rollDie(min, max){
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
rollDie(1,20);

function untilDouble(){
  var stats = []
  var i = 0;
  while (i >= 0){
    var randNum = rollDie(1, 20);
    stats.push(randNum)
    console.log(stats);
    if(stats[i] === stats[i-1]){
      var rolls = i + 1;
      break;
      console.log(rolls);
    }
    i += 1;
  }
  var max = stats[0];
  var min = stats[0];
  var sum = 0;
  for(var j = 0; j < stats.length; j += 1){
    if (stats[j] < min){
      min = stats[j];
    }
    else if(stats[j] >= max){
      max = stats[j]
    }
    sum += stats[j];
  }
  var avg = sum / stats.length
  // console.log(sum);
  return console.log(rolls, max, min, avg);
}
untilDouble();
