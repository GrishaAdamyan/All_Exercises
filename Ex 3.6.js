var a = 100
var b = 600
for(var i = a; i <= b; i ++){
    if(i % 3 == 0 && i % 11 == 0 && i % 7 != 0){
        console.log(i)
    }
}