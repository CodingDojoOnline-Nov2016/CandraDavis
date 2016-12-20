// You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.

function prevLengths(array){
  for (var i = array.length-1; i > 0; i -= 1){
    array[i] = array[i-1].length;
  }
  return array;
}

prevLengths(['some', 'one', 'please', 'substantiate', 'a', 'claim', 'expressly' ]) // 4,3,6,12,1,5,9
