// 1
var sum = 0
var a = +prompt()
var b = +prompt()
for(var i = a; i <= b; i ++){
    sum += i
}
console.log(sum)

// 2
var result = 1
for(var i = 1; i <= 15; i ++){
    result *= i
}
console.log(result)

// 3
var sum = 0
var n = +prompt()
for(var i = 1; i <= n; i ++){
    var number = +prompt()
    sum += number
}
console.log(sum)

// 4
var sum = 0
var n = +prompt()
for(var i = 1; i <= n; i ++){
    var number = +prompt()
    if(number % 2 == 0){
        sum += number
    }
}
console.log(sum)