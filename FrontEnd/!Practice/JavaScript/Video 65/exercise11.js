//let array = [6,5,4,3,2,1]


// const factorial = (a,b) => {
//      return a*b;
// }

// console.log(array.reduce(factorial));

console.log("____________________")

// let number = 6;
// let factorial = 1;

// for (let i = 1; i < number; i++) {
//      factorial *= i ;     
// }
// console.log(factorial)


let a = prompt("Enter a number");
let b = parseInt(a)

let array = []

for (let i = 1; i <= b; i++) {
     array.push(i)
}



const product = (a,b) =>{
     return a*b;
}
console.log(array.reduce(product))