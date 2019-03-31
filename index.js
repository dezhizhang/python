var MinClass = /** @class */ (function () {
    function MinClass() {
        this.list = [];
    }
    MinClass.prototype.add = function (num) {
        this.list.push(num);
    };
    MinClass.prototype.min = function () {
        var minNum = this.list[0];
        this.list.map(function (item, index) {
            if (minNum > item) {
                minNum = item;
            }
        });
        return minNum;
    };
    return MinClass;
}());
var m = new MinClass();
m.add(2);
m.add(1);
m.add(222);
console.log(m.min());
