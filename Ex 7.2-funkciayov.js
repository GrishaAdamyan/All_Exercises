function qarakusi(n, l){
    for(let i = 0; i < n; i++){
        forward(l)
        left(360 / n)
    }
}

qarakusi(4, 100)