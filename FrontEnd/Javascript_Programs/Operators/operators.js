
//! Operators
//^---------------------------------------------------------------------------------------------
//! Arithmethic Operator
// console.log(2+3)
// console.log(2-3)
// console.log(2*3)
// console.log(2/3)
// console.log(2%3)
// console.log(2**3)
//^---------------------------------------------------------------------------------------------
//! Relational Operator
// console.log(2<3)
// console.log(2>3)
// console.log(2=="2")   //* compares the values not data type
// console.log(2==="2")   //* compares the data type and value also
// console.log(2!="2")
// console.log(2!=="2")
// console.log(2>=6)
// console.log(2<=6)
//^---------------------------------------------------------------------------------------------
//! Assignment Operator 
//* Its reassigning value
let x= 25
console.log(x+=1)   //x = x+1
console.log(x-=1)   //x = x-1
console.log(x*=2)   //x = x*2
console.log(x/=2)   //x = x/2
console.log(x%=2)   //x = x%2
console.log(x**=3)  //x = x**3
//^---------------------------------------------------------------------------------------------
//! Logical Operator
//*logical &&
// console.log((5>4)&&(5<7))  // will be true when both values are true
// console.log((4<5)||(5>10))  // will be true when one value is true
// console.log(!(10>20))          // true - false , false - true
//^---------------------------------------------------------------------------------------------
//! Conditional Operator
//* short if
// let res = (5>10)?5:10
// console.log(res)  //* res is 10 because condition is false 
//^---------------------------------------------------------------------------------------------
//! Increament and Decreament operator
//! Increament
// let x = 25
// x++                      //* x= x+1 increament always by 1
// console.log(x)

// let x = 5
// console.log(++x + x++ ) //* 6+6 = 12 

//! Deacreament
// let x = 25
// x--                       //* x= x-91 deacrement always by 1
// console.log(x)

// let x = 5
// console.log(--x + x--) //* 4+4 = 8 
//^---------------------------------------------------------------------------------------------
//*   + is also used as unary operator of converting any data type into number 
// console.log(3+"3")
// console.log(3-"3")    //0
// console.log(3+ +"3")
//^---------------------------------------------------------------------------------------------
//! nullish coelision operator 
// let a = undefined;let b = 30
// let c = a??b
// console.log(c)
//^---------------------------------------------------------------------------------------------