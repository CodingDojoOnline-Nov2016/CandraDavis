function flexibleCountdown(lowNum, highNum, mult) {
  for (var i = highNum; i >= lowNum; i -= mult)
    console.log(i);
}
flexibleCountdown(2,9,3)
