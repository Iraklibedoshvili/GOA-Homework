// primitiuli mnishvneloba sheicavs xolod ert mnishvnelobas.inaxeba stack mexsierebashi.xolo kompleqsuri sheicavs ors 
// da inaxeba heap mexsierebashi

//primitiuli

let name = "Giorgi"
let age ="15"
let isMan= true

//kompleqsuri

let Man = {name:"Giorgi",age:25};
let numbers = [1,2,3,4]

//Leak memory

let leak=[]
function leakMemory(){
    let data= new Array(1000000).fill("leak")
    leak.push(data)
}