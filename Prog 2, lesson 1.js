// 1

var a = 100;
var b = 200;
var p = calcPer(a,b);
var s = calcSq(a,b);
console.log(p,s);

function calcPer(c,d){
   p = 2 * c + 2 * d
   return p
}

function calcSq(e,f){
   s = e * f
   return s
}

// 2

var c = [45, 60, 12, 98, 78, 154, 65];
var m = [15, 98, 45, 33, 78, 98, 100, 56, 98];
var s1 = sumArray(c);
var s2 = sumArray(m);
console.log(s1, s2);


function sumArray(a){
   var sum = 0
   for(var i = 0; i < a.length; i ++){
      sum += a[i]
   }
   return sum
}

// 3

var c = [45,60,12,98,78,154,65];
var b = reverseArray(c);
console.log(b); //պիտի տպի 65,154,78,98,12,60,45

var t = ["php","javascript","html","css","mysql"];
var m = reverseArray(t);
console.log(m); //պիտի տպի mysql, css, html, javascript, php

function reverseArray(a){
   var b = []
   for(var i = 0; i < a.length; i ++){
      b[i] = a[a.length - 1 - i]
   }
   return b
}