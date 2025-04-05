marks = {
  harry: 98,
  rohan: 70,
  aakash: 71,
};

for (const key in marks) {
  console.log(`${key}:${marks[key]}`);
}

let number = 89;

if (number==100)
     {
        console.log("its right number");
     }
     else{
          console.log("try again");
     }

     function mul(a,b,c,d,e){
        const  sum=a+b+c+d+e;
          const mean=sum/5;
          return mean;
     }

const result = mul(48,5,6,7,8);

     console.log("the mean of 5 number is ",result);