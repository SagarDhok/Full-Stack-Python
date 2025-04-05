console.log("sagar is hacker");
console.log("jay is hecker"); //synchronus

setTimeout(function () {
  console.log(" i am inside settimeout");
}, 0);

setTimeout(function () {
  console.log(" i am inside settimeout 2");
}, 0); // Asynchronus

console.log("The end");

const fn = () => {
  console.log("nothing")
}

const callback = (arg) => {
  console.log(arg);
};

const loadScript = (src, callback) => {
  let sc = document.createElement("script");
  sc.src = src;
  sc.onload = callback("harry");
  document.head.appendChild(sc);
};

loadScript =
  ("https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/prism.min.js",
  callback);
  
  cl


