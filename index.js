var Person = /** @class */ (function () {
    function Person(name) {
        this.name = name;
    }
    Person.prototype.run = function () {
        alert(this.name + "\u54C8\u54C8");
    };
    return Person;
}());
var p = new Person('小明');
p.run();
