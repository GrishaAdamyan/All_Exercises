// 1
function f(a, b){
    alert(b * a)
    alert(b - a)
}

f(5, 9) // 45

// 2
function f(a, b){
    alert(b * a)
}

f(5, 9) // 45
f(3, 9)  // 27
f(3, 9)  // 27

// 3
function f(a, b){
    alert(b * a)
    alert(b - a)
}
 
let c = 10
let d = 5

f(c, d) // 45

// 4
let a = 10
function f(){
    let a = 5; 
    function f1() {
        alert(a) // 5
    }
    f1()
}

f()
alert(a)


// 5
function inchVorAnkyun(n, l, x, y, r, g, b, w){
    let ank = 360 / n // 72
    color(r, g, b) //250 25 10
    goto(x, y) // 0 0
    width(w) // 4
    for (let i = 0; i < n; i++) { // 5
        forward(l) // 100
        left(ank) // 72
    }
}

inchVorAnkyun(5, 100, 0, 0, 250, 25, 10, 4)
inchVorAnkyun(3, 90, 200, -200, 10, 250, 10, 3)
inchVorAnkyun(6, 120, 200, -200, 10, 250, 10, 3)

 // 6
 function inchVorAnkyun(n, l, x, y, c = 'red' ){
    let ank = 360 / n // 72
    color(c) //250 25 10
    goto(x, y) // 0 0
    for (let i = 0; i < n; i++) { // 5
        forward(l) // 100
        left(ank) // 72
    }
}

inchVorAnkyun(5, 100, 0, 0, 'red')
inchVorAnkyun(3, 90, 200, -200,'blue')
inchVorAnkyun(6, 120, 200, -200)

// 7
function random(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}
x = f(-350, 350)
y = f(-350, 350)

// 8
function random(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

function triangle(n){
    let x = random(-350, 350)
    let y = random(-350, 350)
    let l = random(50, 100)
    let w = random(1, 7)
    let r = random(0, 90)

    goto(x, y)
    width(w)
    right(r)
    color('blue')
    for(let i = 0 ; i < n; i++){
        forward(l)
        left(360 / n)
    }
}

for(let i = 0; i < 36; i++){
    triangle(3)
}