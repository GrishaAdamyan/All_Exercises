var a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var b = []
for(var i = 0; i < a.length; i ++){
  b[i] = a[a.length-1-i]
}
console.log(b)