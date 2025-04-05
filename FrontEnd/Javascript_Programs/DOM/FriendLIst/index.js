const OutputDiv = document.getElementById("OutputDiv")
const InptElmt = document.getElementById("InptElmt")

let Friendlist = []

function addTodo() {
     Friendlist.push(InptElmt.value)
     displayTodo()     
}

function displayTodo() {
     OutputDiv.textContent = ""
     Friendlist.forEach((element,index) => {
          const NewDiv = document.createElement("div")
          NewDiv.classList.add("NewDiv")
     
          const p = document.createElement("p")
          p.textContent = element

          const deleteButton = document.createElement("button")
          deleteButton.textContent = "Block"
          deleteButton.addEventListener("click",()=> RemoveTodo(index))

          NewDiv.append(p,deleteButton)
          OutputDiv.appendChild(NewDiv)
          

     });
}

function RemoveTodo(index) {
     Friendlist.splice(index,1)
     displayTodo()
     
}