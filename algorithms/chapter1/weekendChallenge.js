// This weekend, for a challenge, create a fill-in-the-blank quiz game. Ask the user’s name, then refer to the user by name as you ask him/her a series of questions that you have stored in an array. Use the prompt() function to get each input from the user and compare it to the answer you expected. When the user enters “Q” (for quit), or perhaps when the user hits [Cancel], exit the game and print the statistics of the game to the console: user name, number of questions answered and questions correct.

function quizGame(){
  var userName = prompt('What is your name?');
  console.log('Hi, ' + userName);
  var questions = ['So, ' + userName + ' where are you from?', 'Where do you live now, ' + userName + '?', userName + ' Do you mind me asking, how old are you?', 'Do you like this game ' + userName + ' ?', 'Have you ever been out of the country ' + userName + ' ?', userName + ' are you married?']
  if(userName != null){
    var count = 0;
    var responArr = [];
    for(i=0; i<questions.length; i++){
      var response = prompt(questions[i]);
      response = response.toLowerCase();
      if (response != null && response != 'q'){
        if(response.length >= 2)
        responArr.push(response);
        count +=1;
      }
      else if (response == 'q') {
        return console.log(userName, count);
      }
    }
  }
}
quizGame();
