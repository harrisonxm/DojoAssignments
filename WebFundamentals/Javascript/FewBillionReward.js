var reward = 0.01;
var sum = reward;
for(var day =1; day <=29; day++){

  reward = reward*2;
  sum += reward;

}
console.log(sum);
