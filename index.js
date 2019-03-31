var Dog = /** @class */ (function () {
    function Dog(name) {
        this.name = name;
    }
    Dog.prototype.eat = function (str) {
        console.log(str);
    };
    return Dog;
}());
var d = new Dog('小花');
d.eat('呀呀');
