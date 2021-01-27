var n = 36
var ankyun = 180 - (((n - 2) / n) * 180)
var l = 100
for(var i = 1; i <= n; i ++){
    goto(0, 0)
    forward(l)
    left(ankyun)
}