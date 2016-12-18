// Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees.

function celsiusToFahrenheit(cDegrees){
  var farhenheit = ((9/5) * cDegrees) + 32;
  farhenheit = farhenheit.toFixed(1);
  return farhenheit + ' degrees Fahrenheit';
}
celsiusToFahrenheit(200);


// Do Fahrenheit and Celsius values equate at a certain number? Scientific calculation can be complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward (descending), checking whether it is equal to the corresponding Fahrenheit value.

function doTheyCompare(){
  for (cTemp = 200; cTemp >= 0; cTemp -= 1) {
    var farhenheit = ((9/5) * cTemp) + 32;
    console.log(cTemp);
    console.log(farhenheit);
  }
}
doTheyCompare();
