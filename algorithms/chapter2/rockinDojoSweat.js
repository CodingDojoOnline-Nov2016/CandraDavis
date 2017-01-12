// Ever since you arrived at the Dojo, you wanted one of those cool Coding Dojo sweatshirts - maybe even more than one. Let-s say they cost $20 (including tax), but friendly Josh will give a 9% discount if you buy two, or a nice 19% discount if you buy three, or a sweet 35% discount if you buy four or more. He only accepts cash and doesn-t have coins, so you have to round up to the nearest dollar. Build a function sweatshirtPricing(num) that, given how many sweatshirts you want, returns the cost.
function sweatshirtPricing(num){
  var sweatShirtPrice = 20
  var totalCost = 0

  if(num === 1){
    return sweatShirtPrice
  }
  else if (num === 2) {
    sweatShirtPrice *= num
    totalCost = sweatShirtPrice - (sweatShirtPrice*.09)
    return Math.ceil(totalCost)
  }
  else if (num === 3 ) {
    sweatShirtPrice *= num
    totalCost = sweatShirtPrice - (sweatShirtPrice*.19)
    return Math.ceil(totalCost)
  }
  else if (num > 3) {
    sweatShirtPrice *= num
    totalCost = sweatShirtPrice - (sweatShirtPrice*.35)
    return Math.ceil(totalCost)
  }
}
sweatshirtPricing(1);
sweatshirtPricing(2);
sweatshirtPricing(3);
sweatshirtPricing(4);
