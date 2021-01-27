var num1 = prompt()
var num2 = prompt()
var nshan = prompt()

num1 = parseFloat(num1)
num2 = parseFloat(num2)

if(nshan === '+'){
    var a = num1 + num2
    console.log(a)
}
else if(nshan === '-'){
    var b = num1 - num2
    console.log(b)
}
else if(nshan === '*'){
    var c = num1 * num2
    console.log(c)
}
else if(nshan === '/'){
    if(num2 === 0){
        console.log('Չի կարելի կատարել բաժանում, երբ բաժանարարը 0 է։')
    }
    else{
        var d = num1 / num2
        console.log(d)
    }
}