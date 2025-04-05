let arr = [1,2,3,4,5]
let newarr= [7,8,9,10,11,12,13]
// for (let i = 0; i < newarr.length; i++) {

//      arr.push(newarr[i])
     
// }
// console.log(arr)/

// for (let i = 0; i < arr.length; i++) {
//      const element = arr[i];
//      newarr.push(element**2);
     
// }
// console.log(newarr);

// let newarr = arr.map((e)=>{
// return e**2;
// })
// console.log(newarr);

function greaterthanten (e) {
     if (e>10){
          return true;
     }
     return false;
}

newarr.filter(greaterthanten); 

console.log(newarr.filter(greaterthanten));

let arr2 = [2,3,4,5]

// const red = (a,b) => {
//  return a+b;                            
// }

// we can write function as below and upper 

function red(a,b){
      return a+b
}


console.log(arr2.reduce(red))
