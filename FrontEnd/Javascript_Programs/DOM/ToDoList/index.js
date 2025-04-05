const OutputDiv = document.getElementById("OutputDiv")
const OutputDiv2 = document.getElementById("OutputDiv2")
const InptElmt = document.getElementById("InptElmt")

let arr = []
let saveitems = []
function addTodo(){
     arr.push(InptElmt.value)
     displayTOdo() 
}

function displayTOdo() {
     
     OutputDiv.textContent = ""
     
     arr.forEach((element,index)=>{
          const NewDiv = document.createElement("div")
          NewDiv.classList.add("NewDiv")
          
          const p = document.createElement("p")
          p.textContent = element

          const saveButton = document.createElement("button")
          saveButton.textContent = "Save"
          saveButton.addEventListener("click",()=>saveTodo(element))

          const deleteButton = document.createElement("button")
          deleteButton.textContent = "❎"
          deleteButton.addEventListener('click',()=>RemoveTodo(index))

          NewDiv.append(p,saveButton,deleteButton)
          OutputDiv.appendChild(NewDiv)
          InptElmt.value= ""
          
          
          
     })
     
}


function displayTOdo2() {
     
     OutputDiv2.textContent = ""
     saveitems.forEach((element,index)=>{
     const NewDiv = document.createElement("div")
     NewDiv.classList.add("NewDiv")
     
     const p = document.createElement("p")
     p.textContent = element

  


     NewDiv.append(p)
     OutputDiv2.appendChild(NewDiv)
     InptElmt.value= ""
     
     
})
}

function saveTodo(element) {
     saveitems.push(element) 
     displayTOdo2() 
        
}


function RemoveTodo(i) 
{
     arr.splice(i,1)
     displayTOdo()
     
}


