var daysUntilMyBirthday = 60;

while(daysUntilMyBirthday > 0)
{
  if(daysUntilMyBirthday >= 30) {
    console.log(daysUntilMyBirthday, "days until my birthday. Such a long time... :(");
    daysUntilMyBirthday -= 1;
  }
  else if(daysUntilMyBirthday >5) {
    console.log(daysUntilMyBirthday, "days until my birthday. It's starting to get near!");
    daysUntilMyBirthday -= 1;
  }
  else{
    console.log(daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY!!!.");
    daysUntilMyBirthday -= 1;
  }
}
console.log("IT'S MY BIRTHDAY, AWESOME!!!!!!!!!!!!!!!!!!!!!!!!!!! LET'S PARTYYYYYYYY!");
