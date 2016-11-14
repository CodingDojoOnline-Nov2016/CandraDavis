var xOdd = [];
var sumInt = xOdd[xOdd.length - 1 + xOdd.length - 2];

  for (var i = -300000; i <= 300,000; i++) {
    if (i % 2 != 0) {
      xOdd.push(i);
    }
    else {
      continue;
    }
  }
console.log(xOdd);
