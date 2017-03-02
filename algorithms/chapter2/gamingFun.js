// Create function rollOne() to return a randomly selected integer between 1 and 6 (inclusive).

function rollOne(min, max){
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
rollOne(1,6)

// Second, create a function playFives(num), which should call rollOne() multiple times – 'num' times, in fact, where 'num' is input parameter to playFives(num). Each time, it should print the value rollOne() returns, and if that return value is 5, also print “That’s good luck!”

function playFives(num){
  for(var i = 0; i <= num; i += 1){
    var randNum = rollOne(1,6);
    console.log(randNum);
    if(randNum === num){
      console.log("That's good luck!");
    }
  }
  return num;
}
playFives(5);
// Third, create a new function named playStatistics(), which should call rollOne() eight times (but not print anything after each call). After the last of these eight calls, it should print out the lowest and highest values that it received from rollOne, among those eight calls.
function playStatistics(){
  var stats = []
  for (var i = 0; i <= 8; i += 1){
    var randNum = rollOne(1, 6);
    stats.push(randNum)
    console.log(stats);
    }
  var max = stats[0];
  var min = stats[0];
  var sum = 0;
  for(var i = 0; i < stats.length; i += 1){
    if (stats[i] < min){
    min = stats[i];
    }
    else if(stats[i] >= max){
    max = stats[i]
    }
  }
 return console.log(max, min);
}
playStatistics();
// Fourth, make a copy of playStatistics and add code to make playStatistics2(), so that at the end (in addition to printing high/low rolls), it also prints the total sum of all eight rolls.
function playStatistics2(){
  var stats = []
  for (var i = 0; i <= 8; i += 1){
    var randNum = rollOne(1, 6);
    stats.push(randNum)
    console.log(stats);
  }
  var max = stats[0];
  var min = stats[0];
  var sum = 0;
  for(var i = 0; i < stats.length; i += 1){
    if (stats[i] < min){
      min = stats[i];
    }
    else if(stats[i] >= max){
      max = stats[i]
    }
    sum += stats[i];
  }
  // console.log(sum);
  return console.log(max, min, sum);
}
playStatistics2();
// Fifth, copy playStatistics2 and add code to it to make playStatistics3(num), so that it will roll as many times as you want, instead of always doing this eight times.
function playStatistics3(num){
  var stats = []
  for (var i = 0; i <= num; i += 1){
    var randNum = rollOne(1, 6);
    stats.push(randNum)
    console.log(stats);
  }
  var max = stats[0];
  var min = stats[0];
  var sum = 0;
  for(var i = 0; i < stats.length; i += 1){
    if (stats[i] < min){
      min = stats[i];
    }
    else if(stats[i] >= max){
      max = stats[i]
    }
    sum += stats[i];
  }
  // console.log(sum);
  return console.log(max, min, sum);
}
playStatistics3(12);
// Finally, make a copy of playStatistics3 and change it to create playStatistics4(num), so that at the end instead of the total sum, it prints the average roll.
function playStatistics4(num){
  var stats = []
  for (var i = 0; i <= num; i += 1){
    var randNum = rollOne(1, 6);
    stats.push(randNum)
    console.log(stats);
  }
  var max = stats[0];
  var min = stats[0];
  var sum = 0;
  for(var i = 0; i < stats.length; i += 1){
    if (stats[i] < min){
      min = stats[i];
    }
    else if(stats[i] >= max){
      max = stats[i]
    }
    sum += stats[i];
  }
  var avg = sum / stats.length
  // console.log(sum);
  return console.log(max, min, sum, avg);
}
playStatistics4(12);
