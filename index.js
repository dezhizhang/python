var Web = /** @class */ (function () {
    function Web(name) {
        this.name = name;
    }
    Web.prototype.eat = function () {
        return this.name;
    };
    Web.prototype.work = function () {
        return this.name;
    };
    return Web;
}());
var w = new Web('小花');
console.log(w.work());
