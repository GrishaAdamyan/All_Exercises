var a = 45
var b = 12
var c = 100

var max = 0

if(b > a){
    if(c > b){
        max = c
    }
    else if(b > c){
        max = b
    }
}
else if(a > b){
    if(a > c){
        max = a
    }
    else if(c > a){
        max = c
    }
}


var min = 0

if(b > a){
    if(c > a){
        min = a
    }
    else if(a > c){
        min = c
    }
}
else if(a > b){
    if(b > c){
        min = c
    }
    else if(c > b){
        min = b
    }
}
console.log(max, min)