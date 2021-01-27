// 1
var a = 100
var b = 350
for(var i = a; i <= b; i ++){
    console.log(i)
}

// 2
for(var i = a; i <= b; i ++){
    if(i % 2 == 0){
        console.log(i)
    }
}

// 3
for(var i = a; i <= b; i ++){
    if(i % 2 == 0 && i % 7 == 0){
        console.log(i)
    }
}

// 4
for(var i = a; i <= b; i ++){
    if(i % 2 == 1){
        console.log(i)
    }
}

// 5
var result = 0
for(var i = a; i <= b; i ++){
    if(i % 2 == 1){
        console.log(i)
        result += i
    }
}
console.log(result)

// 6
var sum = 0
for(var i = a; i <= b; i ++){
    if(i % 2 == 0){
        console.log(i)
        sum += i
    }
}
console.log(sum)

// 7
for(var i = b; i >= a; i --){
    if(i % 2 == 0){
        console.log(i)
    }
}