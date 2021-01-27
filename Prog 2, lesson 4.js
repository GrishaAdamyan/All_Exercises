// 1
class Programmer {
    constructor(email, age, surname, name) {
        this.email = email;
        this.age = age;
        this.surname = surname
        this.name = name;
    }
    email1() {
        console.log(this.email)
    }
    age1() {
        console.log(this.age)
    }
    surname1() {
        console.log(this.surname)
    }
    name1() {
        console.log(this.name)
    }
}

var p = new Programmer('gmail.com', 16, 'Adamyan', 'Grisha')
p.email1()
p.age1()
p.surname1()
p.name1()