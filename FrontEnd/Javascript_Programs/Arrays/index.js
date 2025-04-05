// let arr = [10,"sagar",290]
// // console.log(arr,typeof(arr))

//! lenght
// console.log(arr.length)
// // console.log(arr[1])

//! push
// arr.push(10,20,30)   // add at the end of 

//!unshift
// arr.unshift("100000","jay","karan")   //add at the start of elment

//!shift
// arr.shift()   // removes the first element
// console.log(arr)

//!splice
// let arr = [0,1,2,3,4,5,6,7]
// arr.splice(5,0,"sagar","dhok")   // startindex delete count addelements
// console.log(arr)

//!pop
// let arr = [1,2,3,4,5,6,7]
// arr.pop();arr.push("dhok")
// arr.shift();arr.unshift("sagar")
// arr.splice(3,1,"santosh")
// console.log(arr.indexOf(1))  // if value is not present then give answer -1
// console.log(arr.concat([1111111]))  // use to add array
// console.log(arr)


//!foreach
// let students = ["sagar","jay","karan","ram"]
// students.forEach(function(val,index){   // callback funtion
//      console.log(val+" "+index)
// })

// let arr = [5,6,7,8]
// console.log("SQUARES","INDEX")
// arr.forEach(function(val,index){  // foreach cannot returns values
//      console.log(val*val,"\t",index)
// })

//^-------------------------------------------------------------------------------------------
//! Return whether each value is even or odd
// let arr= [10,3,5,6,7,2,8]
// let EvenOdd = arr.map((val)=> {
//      if (val%2==0){

//           return "even"
//      }
//      else{
//           return "odd"
//      }
// })
// console.log(EvenOdd)

//* tenary operator
// let arr= [10,3,5,6,7,2,8]
// let EvenOdd = arr.map((val)=>(val%2==0)?val:"odd")
// console.log(EvenOdd)

//*map
// let arr = [5,6,7,8]
// let res= arr.map(function(val){  // foreach cannot returns values
//      return val*val
// })
// console.log(res)

// let arr = ["sagar","jay","karan","prathmesh"]
// let res = arr.map((val)=>{
//      // return val[0].toUpperCase()
//      return val.charAt(0).toUpperCase()
// })
// console.log(res)

// let arr = [1,2,3,4,5,6,7]
// let res = arr.map((val)=>val%2==0)
// console.log(res)



//! filter()
// let names = ["rohit sharma","virat kohali","abhishek sharma","mohit sharma"]
// let res = names.filter((val)=> val.endsWith("sharma"))
// console.log(res)
 
// let arr = [1,2,3,4,5,6,7]
// let res = arr.filter((val)=>val%2==0)
// console.log(res)


//! some
//* one should be true then true
// let names = ["rohit sharma","virat kohali","abhishek sharma","mohit sharma"]
// let res = names.some((val)=> val.endsWith("sharma"))
// console.log(res)

//! every
//* every value should be true
// let names = ["rohit sharma","abhishek sharma","mohit sharma"]
// let res = names.every((val)=> val.endsWith("sharma"))
// console.log(res)

//!sort

// let arr = [1,4,7,9,11]
// console.log(arr.sort())              //* without callback  it will sort on first val, lexigraphycally
// console.log(arr.sort((a,b)=>a-b))    //*  asscending
// console.log(arr.sort((a,b)=>b-a))    //*  descending

//! reverse
// let arr = [1,4,7,9,11]
// console.log(arr.reverse())
// console.log([1,4,7,9,11].reverse())


// //! reduce
//* accumulated logic , prev+cur and store in prev
//* can use any value in place of 0
// let arr = [1,2,3,4,5]
// let res = arr.reduce((prev,cur)=>prev+cur,0)
// console.log(res)


// let arr = [];
// let res = arr.reduce((prev, cur) => prev + cur); // Throws TypeErro
//^-------------------------------------------------------------------------------------------
//! objects
// let obj = {
//           username : "sagar",
//           password : 1234,
//      display : function(){
//           console.log("Good Morning")
//      }
// }

// console.log(obj.username,obj["username"])
// console.log(obj.password,obj["password"])
// obj.display()                  //* funtion can be called also which is present in obj
// console.log(Object.keys(obj))  //*gives key
// console.log(Object.values(obj)) //* gives values


//*task
// let arr = [
//        {
//     name: "RRR",
//     year: 2023,
//       },
//      {
//          name: "BAHUBALI",
//          year: 2016,
//       },
//      {
//      name: "KGF",
//      year: 2023,
//      },
// ];
// function movies() {
// arr.forEach((v) => console.log(v.name + " : " + v.year));
// }
// movies();
//^-------------------------------------------------------------------------------------------