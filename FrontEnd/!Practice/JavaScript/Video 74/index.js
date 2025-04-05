let button = document.getElementById("btn");
let ved = document.getElementById("ved");

button.addEventListener("click", () => {
  document.querySelector(".box").innerHTML =
    "<b>YAYY YOU WERE CLICKED</b> enjoy your click";
});


button.addEventListener("dblclick", () => {
     alert("HELLO GUYS I AM UNDER THE WATER ")
});


document.addEventListener("keydown", (e) => {
     console.log(e.key ,e.keyCode)
   });
   