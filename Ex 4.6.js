var arr = [5, 17, 3, 13, 15, 7, 10, 9, 19, 14, 12, 11, 8, 18, 20, 24, 22, 29, 33, 777, 100, 57, 99, 111, 159, 357, 789, 1000, 2, 5555]
var max = 0
var min = 0
for(var i = 0; i < 30; i ++){
    if(arr[min] > arr[i]){
        min = i
    }
    if(arr[max] < arr[i]){
        max = i
    }
}
console.log(arr[min], arr[max])