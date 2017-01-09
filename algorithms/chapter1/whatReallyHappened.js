function whatReallyHappened(){
  var kenny = 'Kenny was killed by a : ';
  var killed = [];
  for(i=0; i<=5; i++){
    var prob = Math.random();
    killed.push(prob.toFixed(2));
  }
  console.log(killed);
  for(i=0; i<killed.length; i++){

    if (killed[i] <= .10){
      console.log(kenny + 'volcanoe');
    }
    else if (killed[i] >.10 &&  killed[i] <= .15) {
      console.log(kenny + 'tsunami');
    }
    else if (killed[i] > .15 && killed[i] <= .20) {
      console.log(kenny + 'earthquake');
    }
    else if (killed[i] > .20 && killed[i] <= .25) {
      console.log(kenny + 'blizzard');
    }
    else if (killed[i] > .25 && killed[i] <= .30) {
      console.log(kenny + 'meteor strike');
    }
    else{
      console.log('Kenny lives!');
    }
  }
  }
whatReallyHappened();
