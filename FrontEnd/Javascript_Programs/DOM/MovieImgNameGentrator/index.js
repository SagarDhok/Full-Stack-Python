const OutputDiv = document.getElementById("output")
const MovieImg = document.getElementById("MovieImg")
const MovieName = document.getElementById("MovieName")

function GenrateMovie() {
     const NewDiv = document.createElement("div")
     NewDiv.classList.add("NewDiv")

     const img = document.createElement("img")
     img.src = MovieImg.value
     img.alt = MovieName.value
     img.height = 100

     const Mname = document.createElement("p")
     Mname.textContent = MovieName.value

     NewDiv.append(img,Mname)
     OutputDiv.appendChild(NewDiv)
     MovieImg.value = ""
     MovieName.value = ""

}