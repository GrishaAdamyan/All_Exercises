var arr = [7, 3, 5, 10, 9, 13, 15, 17, 18, 12]

// 1
result = 0
for(var i = 0; i < 10; i ++){
    result += arr[i]
}
console.log(result)

// 2
console.log(result / arr.length)

// 3
var res = 1
for(var j = 0; j < 10; j ++){
    res *= arr[j]
}
console.log(res)