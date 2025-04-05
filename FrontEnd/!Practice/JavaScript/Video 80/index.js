//  let obj = {
//      name:"sagar",
//      age:19
//  }

//  console.log(obj)

//  let animal = {
//      eats:true
//  };
//  let rabbit = {
//      jumps:true
//  };

//  rabbit.__proto__=animal; //! sets rabbit.[{Prototype}]=animal

class Animal {
  constructor(name) {
    this.name = name;

    console.log("Object is created...");
  }
  eats() {
    console.log("kha raha hu");
  }
  jumps() {
    console.log("uchaal raha hu");
  }
}

class Lion extends Animal {
  constructor(name) {
    super(name);
    console.log("Object is created and he is lion...");
  }
  eats() {
     super.eats()
    console.log("dabake pel raha hu");
  }
}

let a = new Animal("bunny");
console.log(a);

let b = new Animal("cow"); //navin pan banvu shato and same class madhi multiple call object banvu shakto
console.log(b);

let l = new Lion("shera");
console.log(l);
