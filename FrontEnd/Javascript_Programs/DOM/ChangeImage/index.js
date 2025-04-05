
function changetext(){
document.getElementById("vk").textContent = "KING"

}
function changeimage() {
     document.getElementById("img").innerHTML = '<img src="https://wallpapers.com/images/featured-full/virat-kohli-pictures-yc8dfpcjssp3s4se.jpg"  alt="" height ="100px">'
 }
 
 const inputElement = document.getElementById("inp")

function changeinput() {
   if(inputElement.value.length<6){
      alert("Password is less than 6 charcter")
     inputElement.value =  " "
   }
}

const changeDiv = document.getElementById("d")

function HideNot() {
     changeDiv.classList.toggle("hide")
}

function changecolor() {
     const bc = "#"+Math.round(Math.random()*10000).toString(16)
     document.body.style.backgroundColor = bc
}