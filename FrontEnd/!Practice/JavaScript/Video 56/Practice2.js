let age = 498;

if (age > 10 && age < 20) {
  console.log("your age lies between 10 to 20");
} else {
  console.log("your age dont lies between 10 to 20");
}

let day = 1;

switch (day) {
  case 1:
    console.log("you have choosen monday");
    break;
  case 2:
    console.log("you have choosen tuesday");
    break;
  case 3:
    console.log("you have choosen wednesday");
    break;
  case 4:
    console.log("you have choosen thursday");
    break;
}

let car = "omni";

switch (car) {
  case "buggati":
    console.log("you have choosen bugaati");
    break;
  case "omni":
    console.log("you have choosen omni");
    break;
  case "bmw":
    console.log("you have choosen bmw");
    break;
  case "ferrai":
    console.log("you have choosen ferrai");
    break;
}

let x = 30;

if (x % 2 == 0 && x % 3 == 0) {
  console.log("it is divisble by 2 and 3");
} else {
  console.log("its not divisble by 2 and 3");
}

let y = 3;
if (y % 2 == 0 || y % 3 == 0) {
  console.log("it is divisbe 2 or 3");
} else {
  console.log("default");
}

// let man = 13;
// if (man>=18){
//      console.log("you can drive");
// }
// else{
//      console.log("you cannot drive");
// }

// using ternary operator

let z = 7;
z >= 18 ? console.log("you can drive") : console.log("you cannot drive");
