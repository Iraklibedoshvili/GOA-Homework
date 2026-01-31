const div=document.getElementsByTagName("div")
console.log("getElementsByTagName:",div)

const products=document.getElementsByClassName("product")
console.log("All Product class elenents:",products)

const SecondProduct= products[1]
console.log("Product:",SecondProduct.previousElementSibling)

console.log("product",SecondProduct.nextElementSibling)

const FirstProduct=document.getElementById("first product")
console.log("product",FirstProduct.firstChild)

console.log("product:",FirstProduct.lastChild)