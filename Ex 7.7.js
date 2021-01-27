let n = 8

for(var i = 0; n < 8; i ++){
    var l = 100
    color('blue')
    forward(l)
    left(180)
    penup()
    forward(10)
    left(135)
    pendown()
    forward(10)
    left(180)
    penup()
    forward(10)
    right(90)
    pendown()
    forward(10)
    goto(0, 0)
}