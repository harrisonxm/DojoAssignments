
if(MINUTE < 30){
  TIMEOFHOUR = "just after";
}
else{
  TIMEOFHOUR = "almost";
  HOUR += 1;
}

if(PERIOD == "AM"){
  PARTOFDAY = "in the morning";
}
else{
  PARTOFDAY = "in the evening";
}

console.log("It's", TIMEOFHOUR, HOUR, PARTOFDAY);
