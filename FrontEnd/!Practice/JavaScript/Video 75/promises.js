//!  const promiseOne = new Promise(function (resolve, reject) {
//   setTimeout(function () {
//     console.log("Async task is complate");
//     resolve();
//   }, 2000);
// });

//promiseOne.then(function () {
//   console.log("promise is consumed");
// });

// new Promise(function () {
//   setTimeout(() => {
//     console.log("async task 2");
//   }, 2000);
// }).then(function () {
//   console.log("async 2 is resolved");
//! });

//*  const promisethree = new Promise(function (resolve, reject) {
//   setInterval(() => {
//     resolve({ username: "chai", email: "sdhok041@gmail.com" });
//   }, 1000);
// });

// promisethree.then(function (data) {
//   console.log(data);
//*});

//! const promisefour = new Promise((resolve, reject) => {
//   setTimeout(() => {
//     let error = true;
//     if (error == false) {
//       resolve({ username: "sagar", password: "327q82" });
//     } else {
//       reject(`ERROR:something went wrong`);
//     }
//   }, 1000);
// });
// promisefour
//   .then((user) => {

//     return user.username;
//   })
//   .then((username) => {
//     console.log(username);
//   })
//   .catch(function (err) {
//     console.log(err);
//   })
//   .finally(() => {
//     console.log(`Promise is either rsolve or rejected`);
// !   });

// const promisefive = new Promise(function (resolve, reject) {
//   setTimeout(() => {
//     const error = true;
//     if (error == false) {
//       resolve({ name: "sagar", age: "19", profession: "student" });
//     } else {
//       reject(`Error : something went wrong`);
//     }
//   }, 1000);
// });

// async function consumepromisefive() {
//   try {
//     const response = await promisefive;
//     console.log(response);
//   } catch (error) {
//     console.log(error);
//   }
// }
// consumepromisefive();

//! promisefive
//   .then((data) => {
//     console.log(data);
//   })
//   .catch(function (err) {
//     console.log(err);
//!   });

const marvel = new Promise(function (resolve, reject) {
  setTimeout(() => {
    let tony = 8;
    let steve = 80;
    if (tony == steve) {
      resolve(`Bhaicahar on top`);
    } else {
      reject("cheating karta hai tu");
    }
  }, 1000);
});

//* marvel.then((marks) => {
//   console.log(marks);
// }).catch(function (err) {
//   console.log(err)
//* })

async function mcu() {
  try {
    let response = await marvel;
    console.log(response);
  } catch (error) {
    console.log(error);
  }
}

mcu();


//! SYNTAX => WITH ARROW FUNCTION IS BELOW


let prom1 = new Promise ((resolve,reject)=>
{
  setTimeout(function () {
    console.log("Yes i am done");
    resolve("Winner Winner Chiken Dinner")
  },1000);
}
)

prom1.then((a) => {
  console.log(a)
}
)



