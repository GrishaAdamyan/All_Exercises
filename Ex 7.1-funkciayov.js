function erankyun(n, l){
    for(let i = 0; i < n; i++){
        forward(l)
        left(360 / n)
    }
}

erankyun(3, 100)