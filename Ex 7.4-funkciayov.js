function f(n, l, x, y){
    var ankyun = 360 / n
    for(var i = 1; i <= n; i ++){
        goto(x, y)
        forward(l)
        left(ankyun)
    }
}
f(36, 100, 0, 0)