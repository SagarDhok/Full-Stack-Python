//! async function getData() {
//      //intejar getting a data from server
//   return new Promise((resolve, reject) => {
//     resolve(567);
//   }, 3000);
//! }

async function getData() {

  let x = await fetch("https://jsonplaceholder.typicode.com/todos/1")
  let data = x.json()
    // console.log(data)  
    return data
}

async function main() {
  console.log("Loading Modules");

  console.log("Do Something else");

  console.log("Load data");
  let data = await getData();

  console.log(data);

  console.log("process data");

  console.log("task 2");
}

main();

//? data.then(function (v) {
//      console.log(data)                        //!data la yayal time lagte

// console.log("process data")

// console.log("task 2")
//? })


