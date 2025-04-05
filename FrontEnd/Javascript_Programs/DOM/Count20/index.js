const CountVal = document.getElementById("val");
const odev = document.getElementById("odev");

let a = 0;

function incr() {
  a++;
  a % 2 == 0 ? (odev.textContent = "EVEN") && (document.getElementById("main").style.backgroundColor="black") && (document.getElementById("main").style.color="white"): (odev.textContent = "ODD") && (document.getElementById("main").style.backgroundColor="white") && (document.getElementById("main").style.color="black");
  CountVal.textContent = a;
     
  if (a == 21) {
    alert("Cant Increase More than 20");
    CountVal.textContent = 0;
    odev.textContent = "EVEN"
    a = 0
  }
}

function deac() {
  a--;
  a % 2 != 0 ? (odev.textContent = "ODD") && (document.getElementById("main").style.backgroundColor="black") && (document.getElementById("main").style.color="white"): (odev.textContent = "EVEN") && (document.getElementById("main").style.backgroundColor="white") && (document.getElementById("main").style.color="black");
  CountVal.textContent = a
  CountVal.textContent = a;
  if (a < 0) {
    alert("Cant Deacrease less than Zero");
    CountVal.textContent = 0;
    odev.textContent = "EVEN"
    a = 0
  }
}

function reset() {
  CountVal.textContent = 0;
  odev.textContent = "EVEN"
  a = 0;
}

