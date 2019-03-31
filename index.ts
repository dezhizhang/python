
class MinClass{
    public list:number[] = [];
    add(num:number) {
        this.list.push(num);
    }
    min():number{
      let minNum = this.list[0];
      this.list.map((item,index) => {
          if(minNum > item) {
              minNum = item;
          }
      })
      return minNum;
    }
}

let m  = new MinClass();
m.add(2);
m.add(1);
m.add(222);
console.log(m.min());























