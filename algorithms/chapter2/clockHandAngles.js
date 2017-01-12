// Regardless of how hard a Dojo student works (and they should work very hard), they always need time every now and then to unwind - not unlike hands on a clock. Traditional clocks are increasingly uncommon, but most people can still read an analog clock's rotating hands of hours, minutes and seconds.
//
// Create function clockHandAngles(seconds) that, given the number of seconds since 12:00:00, will print the angles (in degrees) of the hour, minute and second hands. As a quick review, there are 360 degrees in a full rotation.
//
// Examples: Given clockHandAngles(3600) (equiveant to 1:00:00), print "Hour Hand: 30 degs. Minute Hand: 0 degs. Second Hand: 0 degs.". For an input parameter seconds of 119730 (equivelant to 9:15:30 plus 24 hrs!), you should log "Hour Hand: 277.745 degs. Minute Hand: 93 degs. Second Hand: 180 degs.". Note: in the second example, the angle for the minute hand is no simply 90 degrees; it has advanced a bit further, because of the additional 30 seconds in that minute so far.
//
// Second: Also calculate and print degrees for an additional "Week Hand" that rotates one each week.

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
  var seconds = min_seconds % 60 // total number of seconds that remain in the num above minutes
  var minute_degrees = 360 / 60 // makes 1 full rotation every 60 minutes

  var second_degrees = 360 / 60 // makes a full rotation every minute

  // to determine the number of degrees, must find the number of weeks, days, hours, seconds and multiply each by it's degree factor.

  console.log('Weeks: ' + Math.trunc(week));
  console.log('Day Hand: ' + Math.trunc(day * day_degrees) + 'degs');
  console.log('Hour Hand: ' + Math.trunc(hour * hour_degrees)+ 'degs');
  console.log('Minute Hand: ' + Math.trunc(minute * minute_degrees )+ 'degs');
  console.log('Second Hand: ' + Math.trunc(seconds * second_degrees ) + 'degs');
}

clockHandAngles(3600);
clockHandAngles(119730);
