let viewstr;

if (views < 100000) {
  viewstr = views ;
} else if (views > 1000000) {
  viewstr = views / +"m";
} else {
  viewstr = views / +"k";
}
function createCard(title, cNAME, views, monthsOld, duration, thumbnail) {
  let html = `<div class="container">
     <div class="card">
       <div class="image">
         <img
           src=${thumbnail}
           alt="image"
         />
         <div class="dur">${duration}</div>
       </div>
       <div class="text">
         <h1>
           ${title}
         </h1>
         <p>${cNAME} . ${views} viwes . ${monthsOld} months ago</p>
       </div>
     </div>
   </div>`;

  document.querySelector(".container").innerHTML =
    querySelector(".container").innerHTML + html;
}

let cards = createCard(
  "Installing vs code & how website works | Sigma Web Development",
  "CodeWithHarry",
  560000,
  5,
  "31.20",
  "https://i.ytimg.com/vi/tVzUXW6siu0/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLB0alxLSXCSEPITzWr-XXUiv1oglQ"
);

console.log(cards);
