abstract class Animale {
    public name:string;
    constructor(name:string) {
        this.name = name;
    }
    abstract eat():any;
}

class Dog extends Animale{
    constructor(name) {
        super(name);
    }
    eat() {
        return this.name + '哈哈';
    }
}

let d = new Dog('小王');
alert(d.eat());
