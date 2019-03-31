


interface Animal{
    name:string;
    eat(str:string):void;
}

class Dog implements Animal{
    name:string;
    constructor(name:string) {
        this.name = name;
    }
    eat(str:string) {
        console.log(str);
    }
}

let d = new Dog('小花');
d.eat('呀呀');

























