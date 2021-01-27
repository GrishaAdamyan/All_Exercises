function vecankyun(n, l){
    for(let i = 0; i < n; i++){
        forward(l)
        left(360 / n)
    }
}

vecankyun(6, 100)