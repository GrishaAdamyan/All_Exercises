// 1
var m = prompt()
m = parseFloat(m)
var n = prompt()
n = parseFloat(n)
var k = prompt()
k = parseFloat(k)
var y = 0
if(k != 0){
    y = (m ** 5) - (100 / k) + (n * 5)
    alert(y)
}
else if(k == 0){
    alert('Tiv@ chi kareli bajanel 0-i')
}

// 2
var n = 8
var l = 100
var ank = 120
for(var i = 0; i < n; i ++){
   forward(l)
   left(ank)
   forward(l / 10)
   goto(0, 0)
   right(ank + 45)
}

// 3
var arr = []
var index = 0
for(var i = 4; i < 671; i ++){
    if(i % 2 == 1){
        arr[index] = i
        index += 1
    }
}
alert(arr)

