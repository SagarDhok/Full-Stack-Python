/* create a buisness name genrator 

  Adjectives :
  Crazy 
  Amazing 
  Fire

  Shop name :
  Engine
  Foods
  Garments

  Another Word :
  Bros
  Limited
  Hub
  */

let random = Math.random();

let first, second, third;
//lets generate the first word
if (random > 0.33) {
  first = "crazy";
  // 0 0.33 0.66 1
} else if (random < 0.66 && random >= 0.33) {
  first = "crazy";
} else {
  first = "fire";
}

//lets generate the second word
random = Math.random();
if (random > 0.33) {
  second = "Amazing ";
  // 0 0.33 0.66 1
} else if (random < 0.66 && random >= 0.33) {
  second = "foods";
} else {
  second = "limited";
}

//lets generate the third word
random = Math.random();
if (random > 0.33) {
  third = "bros";
  // 0 0.33 0.66 1
} else if (random < 0.66 && random >= 0.33) {
  third = "garments";
} else {
  third = "hub";
}

console.log(`${first} ${second} ${third}`);
