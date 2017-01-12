// Change is inevitable (especially when you break a twenty!). Make generateCoinChange(cents). Accept a number of America cents, compute and print how to represent that amount with the smallest number of coins possible. Common American coins are penny (1 cent), nickel (5 cents), dime (10 cents) and quarter (25 cents).
//
// Example: Given generateCoinChange(94):
// 94 cents can be represented by:
//
// quarters:	3
// dimes	1
// nickels:	1
// pennies:	4
// Second: Can you simplify/shorten your code?
//
// Third: Add half-dollar (50 cents) and dollar (100 cents) coins with 40 additional characters or less

function generateCoinChange(coins){
  var dimes_remain = coins % 25 // result gives me how many coins are left after dividing by the value of a quarter
  var nickels_remain = dimes_remain % 10 // result gives me how many coins are left after dividing by the val of a dime
  var pennies_remain = nickels_remain % 5 // result gives me how many pennies are left after dividing by the val of a nickel
  var quarters = Math.trunc(coins / 25)
  var dimes = Math.trunc(dimes_remain / 10)
  var nickels = Math.trunc(nickels_remain / 5)
    console.log('Quarters: ' + quarters);
    console.log('Dimes: ' + dimes);
    console.log('Nickels: ' + nickels);
    console.log('Pennies: ' + pennies_remain);
}
function generateCoinChange(98)
