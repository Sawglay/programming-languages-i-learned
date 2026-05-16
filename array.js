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