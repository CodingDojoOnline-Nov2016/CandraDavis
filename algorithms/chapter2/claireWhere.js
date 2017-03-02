// On New Year’s Eve, have fun but don’t forget your way home! For this challenge create four functions (reset, moveBy, xLocation and yLocation) to track the travels of Claire, a wanderer. Calling reset() moves Claire home to the origin (0,0). The moveBy(xOffset,yOffset) function moves her by those amounts, in those directions. Finally, xLocation() and yLocation() return how far Claire is from home, in X and Y directions respectively. After the calls of reset(), moveBy(1,-2), and moveBy(3,1), subsequently calling xLocation() and yLocation() should return 4 and -1.
//
// Second: create distFromHome(). Assuming she moves diagonally, return her distance from home.
function moveBy(xOffset, yOffset){
  var distance = [];
  distance[0] += xOffset;
  distance[1] += yOffset;
  return distance;
}
function xLocation(){
  var x = moveBy()
  return console.log();;
}
function yLocation(distance){
  return console.log(distance[1]);;
}
function reset(distance){
  distance = [0, 0];
  return console.log(distance);
}
moveBy(1, -2);
moveBy(3, 1);
console.log(moveBy);
