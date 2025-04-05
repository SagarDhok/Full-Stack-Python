const mydiv = document.getElementById("main")
const imageUrl = document.getElementById("url")
const textName = document.getElementById("name")
function GenerateId() {
     const image = document.createElement("img")
     image.src = imageUrl.value
     image.alt = textName.value
     image.height = "100"
     const myName = document.createElement("p")
     myName.textContent = textName.value
     mydiv.append(image,myName)
     imageUrl.value = ""
     textName.value = ""

}

