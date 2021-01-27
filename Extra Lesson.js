// 1
function erankyuni(n, l, x, y) {
    right(90)
    goto(x, y)
    for(let i = 0; i < n; i++){
      forward(l)
      left(360 / n)
    }
    penup()
    forward(l/2)
    right(90)
    pendown()
    forward(50)
    left(180)
}

erankyuni(3, 100, 0, 0)
erankyuni(3, 100, 100, 100)
erankyuni(3, 100, -200, 100)

// 2
let a = prompt('a') //
a = parseFloat(a)
let b = prompt('b')
b = parseFloat(b)
let c = prompt('c')
c = parseFloat(c)

let y = 0

if(c != 0){
y = a ** 3 - b * 3 + 5 - c
alert(y)
}

// 3
let arr = [1, 'ok', 56, 45,  89]

for (let i = 0; i < arr.length; i++) {
    alert(arr[i]) //0 1
}

// 4
function f(a, b) {
    let c = a + b
    return c
}

alert(f(2, 3) == 5)

// 5
var ar1 = [4,5,12,32,100,98,12,32,45,12,32,89];
var ar2 = [98,4,12,32,6,45,12,32,89,100,45, 89];
let arr = []
let count = 0
for (let i = 0; i < ar1.length; i++) {
    for (let y = 0; y < ar2.length; y++) {
        if(i == y && ar1[i] == ar2[y]){ // 
            let tiv = ar1[i] + ar2[y]
            //arr[count++] = tiv
            console.log(tiv);
        }  
    }   
}

// 6
color("#031101")
let m=20;

setInterval(function(){
   //clear()
   drawSquare(m)
   left(10)
   m+=2
},50)


function drawSquare(side){
  forward(side)
  left(90)
  forward(side)
  left(90)
  forward(side)
  left(90)
}

// 7
function rand(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}

function pattern() {
  let l, n, x, y, r, g, b, w
  l = rand(10, 500)
  n = rand(3, 100)
  x = rand(-350,350)
  y = rand(-350,350)
  r = rand(0, 255)
  g = rand(0, 255)
  b = rand(0, 255)
  w = rand(1, 50)


  width(w)
  color(r, g, b)
  for (let i = 0; i < n; i++) { 
     goto(0, 0)
    forward(l)
    left(360 / n)
  }
}


pattern()

setInterval(pattern, 50)