function finalCountdown(multiple, start, limit, exception){
  while (start < limit){
    multiple += multiple;
    // if (multiple = exception) {
    //   continue;
    // }
    console.log(multiple);
  }
}

finalCountdown(3, 5, 17, 9);
