// 1.
var nvar = prompt();

nvar = parseFloat(nvar);

if(nvar % 2 === 0){
    console.log('Զույգ է։');
}
else{
    console.log('Կենտ է։');
}

// 2.
if(nvar % 3 === 0){
    console.log('3-ի բազմապատիկ է։');
}
else{
    console.log('3-ի բազմապատիկ չէ։');
}

// 3.
if(nvar % 3 === 0 && nvar % 2 === 0){
    console.log('Միաժամանակ 3-ի և 2-ի բազմապատիկ է։');
}
else{
    console.log('Միաժամանակ 3-ի և 2-ի բազմապատիկ չէ։');
}