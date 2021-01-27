var n = 3
var ankyun = 180 - (((n - 2) / n) * 180)
var l = 100
for(var i = 1; i <= n; i ++){
    forward(l)
    left(ankyun)
}