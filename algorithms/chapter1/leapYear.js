function leapYear(num) {
  if (num % 4 == 0 && num % 100 == 0 ) {
    console.log(num + "is not a leap year");
  }
  else if (num % 4 == 0 || num % 400 == 0) {
    console.log(num + " is a leap year!")
  }
  else {
    console.log(num + " is not a leap year");
  }
}

leapYear(2016);
