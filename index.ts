

class Person{
    public name:string;
    constructor(name:string) {
        this.name = name;
    }
    run() {
        alert(`${this.name}哈哈`)
    }
}

let p = new Person('小明');
p.run();
