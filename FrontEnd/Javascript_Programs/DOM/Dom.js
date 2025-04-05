//^-------------------------------------------------------------------------------------------------
//!Dom Selection

// console.log(document)

// console.log(document.getElementsByTagName("h1")[1])
// console.log(document.getElementsByClassName("tamdi")[0])
// console.log(document.getElementById("chitti"))

// console.log(document.getElementsByClassName("btn")[0])  //*it get stored in array thats why index
// console.log(document.getElementsByTagName("btn")[0])    //* it get stored in array thats why index
// console.log(document.getElementById("btn"))             //* id name can be only one so no need to write index

//* it selects only first element
// console.log(document.querySelector(".btn"))  //* selects class
// console.log(document.querySelector("#btn"))  //* selects id
// console.log(document.querySelector("btn"))   //*selects tag

//* it selects all element
// console.log(document.querySelectorAll(".btn"))
// console.log(document.querySelectorAll("#btn"))
// console.log(document.querySelectorAll("btn"))
//^-------------------------------------------------------------------------------------------------
//! Dom Manipulation

//* both are same but
//* textcontent = whatever the text inside and wont consider css
//* innertex = it considers css
// function clickme() {
//      const p = document.getElementById("para")
//      // p.textContent = "MY NAME IS ANTHONY GUNJWISH"
//      p.innerHTML = "<strong>My name is anthony gunjlawish</strong>" //*can update html tags also
//      // console.log(p.textContent)
//      // console.log(p.innerText)
// }
// let a = document.getElementById('para')
// function clickme(){
//  a.innerText =  "  My name is anthony gunjalwish "
// }

// function pressme(){
//     a.innerHTML = "<h1> My name is anthony gunjalwish </h1>"
// }
//^-------------------------------------------------------------------------------------------------
// function myfun() {
//     const inp = document.getElementById("inp")
//     const h1 =    document.getElementById("h1")
//      document.getElementById("h1").textContent = inp.value
//      document.getElementById("h1").classList.toggle("dark")
//      document.getElementById("h1").style.color = "blue "
//     }

//^-------------------------------------------------------------------------------------------------\
// const mydiv = document.getElementById("h1")
// function myfun() {
//     const para = document.createElement("p")    //* any name
//     para.textContent = "Hello World"
//     mydiv.appendChild(para)           //* append single child
// }

// let c = 0
// const mydiv = document.getElementById("h1")
// function myfun() {
//     const para = document.createElement("p")    //* any name
//     para.textContent = c++
//     mydiv.appendChild(para)           //* append single child
// }