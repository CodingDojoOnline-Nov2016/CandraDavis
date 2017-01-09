// For an additional challenge, add ‘-’ signs to scores in the bottom two percent of A, B, C and D scores, and “+” signs to the top two percent of B, C and D scores (sorry, Mr. Cerise never gives an A+).
// Mr. Cerise teaches high school math. Write a function that assigns and prints a letter grade, given an integer representing a score from 0 to 100? Those getting 90+ get an ‘A’, 80-89 earn ‘B’, 70-79 is a ‘C’, 60-69 should get a ‘D’, and lower than 60 rece
function grade(score){
  if (score > 0 && score <= 59){
    console.log('Score: ' + score + ' Grade: F');
  }
  else if (score >= 60 && score < 70) {
    if(score >= 63 && score < 68){
    console.log('Score: ' + score + ' Grade: D');
    }
    else if(score >= 60 && score < 63) {
      console.log('Score: ' + score + ' Grade: D-');
    }
    else if (score >= 68 && score < 70) {
      console.log('Score: ' + score + ' Grade: D+');
    }
  }
  else if(score >= 70 && score < 80){
    if(score >= 73 && score < 78) {
      console.log('Score: ' + score + ' Grade: C');
    }
    else if(score >= 70 && score < 73) {
      console.log('Score: ' + score + ' Grade: C-');
    }
    else if (score >= 78 && score < 80) {
      console.log('Score: ' + score + ' Grade: C+');
    }
  }
  else if (score >=80 && score < 90) {
    if (score >= 83 && score < 88) {
    console.log('Score: ' + score + ' Grade: B');
    }
    if(score >= 80 && score < 83) {
      console.log('Score: ' + score + ' Grade: B-');
    }
    else if (score >= 88 && score < 90) {
      console.log('Score: ' + score + ' Grade: B+');
    }
  }
  else if (score >=90 && score <=100) {
    console.log('Score: ' + score + ' Grade: A');
  }
  else{
    console.log('Please enter a valid score between 0 and 100');
  }
}
grade(5);
grade(65);
grade(79);
grade(82);
grade(95);
grade(-4);
grade(104);
