// Return to your previous clockHandAngles solution. Allow fractional values for input seconds, but change your implementation to print only integer values for angles (in degrees) of the various hands.

// there are 604800 seconds per week
// there are 7 days per week
// there are 86400 seconds per day
// there are 24 hours per day
// there are 3600 seconds per hour
// there are 60 minutes per hour
// there are 60 seconds per minute
//convert seconds to weeks, days, hours, and minutes

function clockHandAngles(num){
  var week = num / 604800 // stores how many weeks of seconds are in the num
  var day_seconds = num % 604800  // the result = seconds above weeks

  var day = day_seconds / 86400 // stores how many days of seconds remain in the num
  var hour_seconds = day_seconds % 86400 // the result = how many seconds remain above days
  var day_degrees = 360 / 7 // makes 1 full rotation every 7 days

  var hour = hour_seconds / 3600 // how many hours of seconds remain in the num
  var min_seconds = hour_seconds % 3600 // what remains is the number of seconds above hours
  var hour_degrees = 360 / 12 // makes 1 full rotation every 12 hours

  var minute = min_seconds / 60 // how many minutes of seconds remain in the num
  var seconds = min_second % 60 // total number of seconds that remain in the num above minutes
  var minute_degrees = 360 / 60 // makes 1 full rotation every 60 minutes

  var second_degrees = 360 / 60 // makes a full rotation every minute

  // to determine the number of degrees, must find the number of weeks, days, hours, seconds and multiply each by it's degree factor.

  console.log('Weeks: ' + Math.trunc(week));
  console.log('Day Hand: ' + Math.trunc(day * day_degrees) + 'degs');
  console.log('Hour Hand: ' + Math.trunc(hour * hour_degrees)+ 'degs');
  console.log('Minute Hand: ' + Math.trunc(minute * minute_degrees )+ 'degs');
  console.log('Second Hand: ' + Math.trunc(seconds * second_degrees ) + 'degs');

}
