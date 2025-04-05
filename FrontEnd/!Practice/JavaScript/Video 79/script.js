let a = prompt("Enter first number");
let b = prompt("Enter second number");

if (isNaN(a) || isNaN(b)) {
  throw SyntaxError("This is not allowed");
}

let sum = parseInt(a) + parseInt(b);

function main() {
  let x = 5;
  try {
    console.log("The sum is ", sum * x);
    return true;
  } catch (error) {
    console.log("error  aa gaya bhai");
    return false;
  }
  {
    console.log("files are closed and db connection lost");
  }
}

let c = main();
