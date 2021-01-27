// 1
function f(tiv, ast) {
    let sum = 1
    for (let i = 0; i < ast; i++) {
        sum *= tiv
    }
    console.log(sum);  
}

f(2, 3)
f(4, 3)

// 2
function f(tiv, ast) {
    let sum = 1
    for (let i = 0; i < ast; i++) {
        sum *= tiv
    }
    return sum
}

console.log(f(2, 3))

// 3
function f(arg){
    if(arg > 0){
        return 'drakan'
    }
    else if(arg < 0){
        return 'bacasakan'
    }
    else if(arg == 0){
        return 0
    }
    else if(isNaN(arg)){
        return 'string'
    }
}

// 4
function erankyun(n, l, x, y){
    let ank = 360 / n
    right(30)
    forward(l)
    right(ank)
    forward(l)
    right(ank)
    forward(l)
    left(180)
    penup()
    forward(l / 2)
    right(90)
    pendown()
    forward(50)
}
erankyun(3, 100, 0, 0)

// 5
function f(n, l, x, y) {
    goto(x, y)
    right(90)
    for (let i = 0; i < n; i++) {
        forward(l)
        left(360 / n)
    }
    penup()
    forward(100 / 2)
    right(90)
    pendown()
    forward(50)
    left(180)
}

f(3, 100, 100, 100)
f(3, 100, -200, 200)
f(3, 100, 200, 100)

// 6
l1 = 100
l2 = 200
for(var i = 0; i < 48; i ++){
  color('green')
  forward(l1)
  goto(0, 0)
  right(360 / 96)
  color('purple')
  forward(l2)
  goto(0, 0)
  right(360 / 96)
}

// 7
for (let i = 0; i < 96; i++) {
    goto(0, 0)
    if(i % 2 == 0){
        color('purple')
        forward(200)
    }else if(i % 2 == 1){
        color('green')
        forward(100)
    }
    left(360 / 96)
}

// 8
goto(0, -200)
function f(n, l){
  for(let i = 0; i < n; i++){
        forward(l)
        left(360 / n)
  }
}
right(90)
for(let i = 3; i < 15; i++){
    f(i, 100)
}