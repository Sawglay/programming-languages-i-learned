// let mixture = new Array('dog', 20, 1.3, true)  //Old Form
let mixture = ['dog', 20, 1.3, true]  // New Form
let bobo = mixture[0]
console.log(bobo);

mixture[4] = "hlaing min han"  //adding new array
// console.log(mixture[0]);
console.log(mixture);

mixture[3] = false  //Overwrite
console.log(mixture);




let fruits = ['apple', 'mango']
fruits[2] = "orange"

console.log(fruits[fruits.length - 1]);
console.log(fruits[2]);




// nested array = [[]]
let arr = [['a', 'b', 'c'], [1, 2, 3]];
console.log(arr);
console.log(arr[0][2]);
arr[0][3] = "d"
console.log(arr);

let NNA = [[0,1,2],['a','x','d'],[12]]




//spread operators = ...    //deleting [], without deleting the value in []

let data1 = [1,2,3]
let data2 = [4,5,6]
let result = [...data1, ...data2]
console.log(result);

// function add(a,b){
//     console.log(a+b);
    
// }

// let num = [1,2];
// add(...num);






//destructuring 

let data = ['MgMg', 22, "TTU"]
// let name = data[0]
// let age = data[1]
// let school = data[2]
// console.log(name, age, school);

let [name, age, school] = data
console.log(name, age, school);

function add([a,b]){
    console.log(a+b);
    
}

add([1,2]);

