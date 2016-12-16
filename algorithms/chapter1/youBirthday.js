function yourBirthday(month, day) {
  if(month == 5 || month == 22 && day == 22 || day == 5)
    console.log('How did you know?');
  else {
    console.log('Just another day....');
  }
}
yourBirthday(5,22);
