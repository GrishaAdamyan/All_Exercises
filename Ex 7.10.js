goto(100, -100)
var l = 200
var ank = 120
for(var i = 1; i < 10; i ++){
    forward(l)
    left(ank)
    forward(l - 7)
    left(ank)
    forward(l - 18)
    left(ank)
    l = l - 30
}