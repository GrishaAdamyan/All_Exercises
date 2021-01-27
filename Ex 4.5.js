var arr = [7, 3, 5, 10, 9, 13, 15, 17, 18, 12]

// 1
for(var i = 0; i < arr.length; i ++){
    if(arr[i] % 2 == 0){
        console.log(arr[i])
    }
}

// 2
for(var i = 0; i < arr.length; i ++){
    if(i % 2 == 0){
        console.log(arr[i])
    }
}

// 3
for(var i = 0; i < arr.length; i ++){
    if(arr[i] % 2 == 1){
        console.log(arr[i])
    }
}