let n = 8

for(var i = 0; i < n; i ++){
    var l = 150
    color('yellow')
    forward(l)
    left(180)
    penup()
    forward(10)
    left(90)
    pendown()
    forward(10)
    left(180)
    penup()
    forward(10)
    pendown()
    forward(10)
    goto(0, 0)
    left(45)
}