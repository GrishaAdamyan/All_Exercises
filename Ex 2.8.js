var t = prompt('Enter temperature.');

t = parseFloat(t);

if(t <= 18){
    console.log('Ցուրտ է։');
}
else if(18 < t && t < 24){
    console.log('Հաճելի է։');
}
else if(t >= 24){
    console.log('Շոգ է։');
}