// function sagar(){
//      console.log("My name is sagar")
// }
// console.log("Hello World ")
// sagar()


// function display(n){
//      console.log(`My name is ${n}`)
// }
// display("Sagar")


// function add(a,b) {
//       c = a+b
//      console.log(`(${a},${b})=${c} `)
// }

// // a = 10
// // b = 20
// add(2)


// function resop(a,b,...c){    //rest operator ...   should be last
//      console.log(a,b,c)
// }
// resop(10,20,30,40,"sagar","jay",89)


// function spread(a,...b)
// {
//      let arr = [29,30,...b,31,32]
//      console.log(a,b,arr)
// }
// spread(10,"sagar",20,30,40,50)


// function fruits(a,...b){   // rest operator
// //     console.log(a,b)
// let arr = [...b,"Watermelon"]   // spread operaor
// console.log(arr)

// }
// fruits("apple","mango","banana","pineapple ")

// function values(x,y,...z){   //res operator take the value 
//      console.log(x,y,z)
//     let arr = [...z,"sagar"]  // spread opertor unpack the value
// //     let p = [z,"sagar"] //without array it is nested array
// //     console.log(arr)
//     print(p)
  
// }
// values(10,20,30,40,50)


// function rtype(a,b){
//      return a+b
    
// }
//  let res = rtype(10,20)
// console.log(res)


// function sum(a,b){
//      console.log(a+b)
//   }
//   sum(2) 



// var sd = function(){
//    console.log("Sagar dhok")
// }
// // sd()    //Sagar dhok
// //console.log(sd)  // [Function: sd]





//* arrow funtion


// const sd = ()=>{
//    console.log("My name is anthony gunjalsh")
// }
// sd()


// const sd = ()=>console.log("My name is anthony gunjalsh")   // one statement can be wriiten without {} 
// sd()


// function x(){
//    console.log("Sagar")
// }

// function y(a,b){
//    b()
//    console.log(a)
// }

// y("dhok",x)

// const fun6 = ()=>{
//    console.log("My name is anthony gunjalwish ")
// }

// function x(a,b) {
//      b()
//      console.log(a)
// }
// x(5,fun6)



//*anonymous funtion
// (function (){
//    console.log("hiiiiiiiiiiiiii")
// })()

//* inner outer funtion 
// function outer() {
//      let c = 0
//      function inner(){
//         c++
//       console.log(c)
//      }
//     return inner
// }
// let x = outer()
// console.log(x)
// x()
// x()
