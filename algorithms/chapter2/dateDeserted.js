// Help Eduardo track what day of the week it is. Create a weekdayName(weekdayNum) function that, given a number between 1 and 7, will console.log a string containing the day of the week for that number (given 1, log "Sunday"). Use a SWITCH statement.

function weekdayName(weekdayNum){
  var day = weekdayNum;
  switch (day) {
    case 1: console.log("Sunday");
      break;
    case 2: console.log("Monday");
      break;
    case 3: console.log("Tuesday");
      break;
    case 4: console.log("Wednesday");
      break;
    case 5: console.log("Thursday");
      break;
    case 6: console.log("Friday");
      break;
    case 7: console.log("Saturday");
      break;
    default: console.log("Please enter a valid number between 1 and 7");
  }
}
weekdayName(3);
// Expand weekdayName() to create weekdayName2(dayNum) accepting numbers up to 365. Return weekday as before, given the number of days total. "Sunday" still corresponds to 1.
function weekDayName2(dayNum){
  // I have to figure out how to simplify the number entered to a value of 1 to 6
  switch (date) {
    case 1: console.log("Sunday");
      break;
    case 2: console.log("Monday");
      break;
    case 3: console.log("Tuesday");
      break;
    case 4: console.log("Wednesday");
      break;
    case 5: console.log("Thursday");
      break;
    case 6: console.log("Friday");
      break;
    case 7: console.log("Saturday");
      break;
    default: console.log("Please enter a valid number between 1 and 7");
  }
}
weekDayName2();
// Create a new function someDays() that calls weekDayName2() seventeen times, with randomly generated integers as high as 365. Log each result string. If it is a weekday, add the phrase "Work hard!", and if it is a weekend day, add "Enjoy your day off!"
function someDays(){
  var min = Math.ceil(1)
  var max = Math.floor(365)
  for(var i = 0; i <= 17; i += 1){
    var randNum = Math.floor(Math.random() * (max - min + 1)) + min
    console.log(randNum);
    if(randNum === 7 || 1) {
      console.log("Enjoy your day off!");
      weekDayName2(randNum);
    }
    else{
      console.log("Work hard!");
      weekDayName2(randNum);
    }
  }
}
someDays();
// Build function monthName(monthNum) that, given a number from 1 to 12, returns a string containing month for that number ("May" corresponds to 5). Use an array, without loops.
function monthName(monthNum){
  var monthsArr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  return console.log(monthsArr[monthNum - 1]);
}
monthName(5);
// Now expand monthName() to create monthToDays(monthNum), returning the number of days in that month, in the year 2017. Hint: use a SWITCH statement for the days in each month.
function monthToDays(monthNum){
  var monthsArr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  var month = monthNum - 1;
  switch (month) {
    case 0: console.log(monthsArr[month] + " : 31 days");
      break;
    case 1: console.log(monthsArr[month] + " : 28 days");
      break;
    case 2: console.log(monthsArr[month] + " : 31 days");
      break;
    case 3: console.log(monthsArr[month] + " : 30 days");
      break;
    case 4: console.log(monthsArr[month] + " : 31 days");
      break;
    case 5: console.log(monthsArr[month] + " : 30 days");
      break;
    case 6: console.log(monthsArr[month] + " : 31 days");
      break;
    case 7: console.log(monthsArr[month] + " : 31 days");
      break;
    case 8: console.log(monthsArr[month] + " : 30 days");
      break;
    case 9: console.log(monthsArr[month] + " : 31 days");
      break;
    case 10: console.log(monthsArr[month] + " : 30 days");
      break;
    case 11: console.log(monthsArr[month] + " : 31 days");
      break;

    default: console.log("Please enter a valid number between 1 and 12");
  }
}
monthToDays(7);
// Despite using his ember expertise to create a glowing SOS visible from space, the days go by and sadly Eduardo is still not rescued. Is it spring yet? It might as well be. Build on monthName() to create dayToMonth(dayNum). If given a day number since the year began, return the current month (assume it is not a Leap Year). Given 75, return "March".
function dayToMonth(dayNum){
  var monthsArr = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

  switch (true) {
    case dayNum < 1 || dayNum === 0: console.log("Please enter a valid number between 1 and 365");
    break;
    case dayNum < 31: console.log(monthsArr[0]); // Jan = 31
      break;
    case dayNum <= 59 && dayNum > 31 : console.log(monthsArr[1]); // Feb = 28
      break;
    case dayNum <= 90  && dayNum > 59: console.log(monthsArr[2]); // Mar = 31
      break;
    case dayNum <= 120 && dayNum > 90: console.log(monthsArr[3]); // Apr = 30
      break;
    case dayNum <= 151 && dayNum > 120: console.log(monthsArr[4]); // May = 31
      break;
    case dayNum <= 181 && dayNum > 151: console.log(monthsArr[5]); // Jun = 30
      break;
    case dayNum <= 212 && dayNum > 181: console.log(monthsArr[6]); // Jul = 31
      break;
    case dayNum <= 243 && dayNum > 212: console.log(monthsArr[7]); // Aug = 31
      break;
    case dayNum <= 273 && dayNum > 243: console.log(monthsArr[8]);  // Sep = 30
      break;
    case dayNum <= 304 && dayNum > 273: console.log(monthsArr[9]); // Oct = 31
      break;
    case dayNum <= 334 && dayNum > 304: console.log(monthsArr[10]); // Nov = 30
      break;
    case dayNum <= 365 && dayNum > 334: console.log(monthsArr[11]); // Dec = 31
      break;
    default: console.log("Please enter a valid number between 1 and 365");
  }
}
dayToMonth(323);
// Eduardo builds a Dojo bootcamp on the island. Initially his students only find Ninja Gold in caves, but eventually, even his tree sloths can write code quickly! Dojo classes meet Monday thru Friday, so let’s reincorporate weekday to our calculations. Construct fullDate(dayNum) to accept the number of days so far in 2017, and return a full date string. He hardly remembers that fateful New Year’s Eve party, but he knows it was a Saturday. Given 142, return "Monday, May 22, 2017".
function fullDate(dayNum){

}
// Times flies when you’re at a Dojo – months in fact. Build fullDate2(dayNum) that will be given a 4-digit integer: the days that have passed since December 31, 2016. This number can stretch into future years! You can assume that any year number divisible by four is a leap year and has a 29- day February. Given 8475, return "Thursday, March 15, 2040".
function fullDate2(dayNum){

}
// Eduardo hacks the Google Maps API and adds this long-forgotten island back onto the map. Soon he is rescued! News of his Hemingway-like stoicism made him famous for centuries. Build fullDate3(dayNum) to handle days up to 140,000! Note: years 2100, 2200, and 2300 are not leap years (although 2400 is). Given 139947, return "Tuesday, February 29, 2400".
function fullDate3(dayNum){

}
