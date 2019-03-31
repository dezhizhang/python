
// class MinClass{
//     public list:number[] = [];
//     add(num:number) {
//         this.list.push(num);
//     }
//     min():number{
//       let minNum = this.list[0];
//       this.list.map((item,index) => {
//           if(minNum > item) {
//               minNum = item;
//           }
//       })
//       return minNum;
//     }
// }

// let m  = new MinClass();
// m.add(2);
// m.add(1);
// m.add(222);
// console.log(m.min());

class MinClass<T>{
    public list:T[] = [];
    add(value:T):void {
        this.list.push(value)
    }
    min():T{
        let minNum = this.list[0];
        for(let i=0;i<this.list.length;i++){
            if(minNum > this.list[i]){
                minNum = this.list[i];
            }
        }
        return minNum;
    }

}

let m = new MinClass<number>();
m.add(33);
m.add(1);
m.add(44);
console.log(m.min());


























