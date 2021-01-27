// 1
var m = 8
var n = 8
matrix = []
for (let y = 0; y < m; y++) {
    matrix[y] = []
    for (let x = 0; x < n; x++) {
        if (x == y) {
            matrix[y][x] = 1
        }
        else {
            matrix[y][x] = 0
        }
    }
}
var side = 30
function setup() {
    createCanvas(matrix[0].length * side, matrix.length * side);
    background('#acacac');
}
function draw() {
    for (var y = 0; y < matrix.length; y++) {
        for (var x = 0; x < matrix[y].length; x++) {
            if (matrix[y][x] == 0) {
                fill('#acacac')
                rect(x * side, y * side, side, side)
            }
            else if (matrix[y][x] == 1) {
                fill(0, 255, 0)
                rect(x * side, y * side, side, side)
            }
        }
    }
}

// 2
var m = 8
var n = 8
matrix = []
for (let y = 0; y < m; y++) {
    matrix[y] = []
    for (let x = 0; x < n; x++) {
        if (x == 8 - y - 1) {
            matrix[y][x] = 1
        }
        else {
            matrix[y][x] = 0
        }
    }
}
var side = 30
function setup() {
    createCanvas(matrix[0].length * side, matrix.length * side);
    background('#acacac');
}
function draw() {
    for (var y = 0; y < matrix.length; y++) {
        for (var x = 0; x < matrix[y].length; x++) {
            if (matrix[y][x] == 0) {
                fill('#acacac')
                rect(x * side, y * side, side, side)
            }
            else if (matrix[y][x] == 1) {
                fill(255, 0, 0)
                rect(x * side, y * side, side, side)
            }
        }
    }
}

// 3
var m = 8
var n = 8
matrix = []
for (let y = 0; y < m; y++) {
    matrix[y] = []
    for (let x = 0; x < n; x++) {
        if (x <= 8 - y - 1) {
            matrix[y][x] = 1
        }
        else {
            matrix[y][x] = 0
        }
    }
}
var side = 30
function setup() {
    createCanvas(matrix[0].length * side, matrix.length * side);
    background('#acacac');
}
function draw() {
    for (var y = 0; y < matrix.length; y++) {
        for (var x = 0; x < matrix[y].length; x++) {
            if (matrix[y][x] == 0) {
                fill('#acacac')
                rect(x * side, y * side, side, side)
            }
            else if (matrix[y][x] == 1) {
                fill('yellow')
                rect(x * side, y * side, side, side)
            }
        }
    }
}

// 4
var m = 8
var n = 8
matrix = []
for (let y = 0; y < m; y++) {
    matrix[y] = []
    for (let x = 0; x < n; x++) {
        if ((x + y) % 2 == 0) {
            matrix[y][x] = 1
        }
        else {
            matrix[y][x] = 0
        }
    }
}
var side = 30
function setup() {
    createCanvas(matrix[0].length * side, matrix.length * side);
    background('#acacac');
}
function draw() {
    for (var y = 0; y < matrix.length; y++) {
        for (var x = 0; x < matrix[y].length; x++) {
            if (matrix[y][x] == 1) {
                fill('black')
                rect(x * side, y * side, side, side)
            }
            else if (matrix[y][x] == 0) {
                fill('white')
                rect(x * side, y * side, side, side)
            }
        }
    }
}

// 5
var side = 30
function setup() {
    createCanvas(11 * side, 11 * side);
    background('#acacac');
}
function draw() {
    for (var y = 0; y < 11; y++) {
        for (var x = 0; x < 11; x++) {
            if (x != 0 && y != 0) {
                text(x * y, side * y + 10, side * x + 10, 48, 48)
            }
            else if (x == 0 && y != 0) {
                text(y, x + 10, y * side + 10, 48, 48)
            }
            else if (x != 0 && y == 0) {
                text(x, x * side + 10, y + 10, 48, 48)
            }
        }
    }
}