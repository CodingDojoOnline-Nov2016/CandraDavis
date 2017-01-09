// Mr. Cerise teaches high school math. Write a function that assigns and prints a letter grade, given an integer representing a score from 0 to 100? Those getting 90+ get an ‘A’, 80-89 earn ‘B’, 70-79 is a ‘C’, 60-69 should get a ‘D’, and lower than 60 rece
function grade(score){
  if (score > 0 && score <= 59){
    console.log('Score: ' + score + ' Grade: F');
  }
  else if (score >= 60 && score < 70) {
    console.log('Score: ' + score + ' Grade: D');
  }
  else if (score >= 70 && score < 80) {
    console.log('Score: ' + score + ' Grade: C');
  }
  else if (score >= 80 && score <90 ) {
    console.log('Score: ' + score + ' Grade: B');
  }
  else if (score >=90 && score <=100 ) {
    console.log('Score: ' + score + ' Grade: A');
  }
  else{
    console.log('Please enter a valid score between 0 and 100');
  }
}
grade(5);
grade(65);
grade(75);
grade(85);
grade(95);
grade(-4);
grade(104);
