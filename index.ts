interface Animal{
    eat():string;
}

interface Person extends Animal{
    work():string;
}

class Web implements Person{
    name:string;
    constructor(name:string){
        this.name = name;
    }
    eat():string {
        return this.name;
    }
    work():string {
        return this.name;
    }
}

let w = new Web('小花');
console.log(w.work());

























