const countValue = document.getElementById("count");
console.log(countValue.textContent);

a = 0;
function incr() {
  a++;
  countValue.textContent = a;
}

function decr() {
     a--
     countValue.textContent=a
}

function res(){
     a = 0
     countValue.textContent = 0
}