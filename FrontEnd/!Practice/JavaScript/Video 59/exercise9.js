// Faulty Calculator
// This calculator performs wrong oprrations

let random = Math.random();
let a = prompt("Enter first number");
console.log(random);
let c = prompt("Enter operation");
let b = prompt("Enter second number");

let obj = {
  "+": "-",
  "*": "+",
  "-": "/",
  "/": "**",
};

if (random > 0.1) {
  

  //or
  alert(`the result is  ${eval( `${a} ${c}  ${b}`)}`);

} else {
  c = obj(c);
  alert(`the result is  ${` ${a} ${c}  ${b}`}`);

}
