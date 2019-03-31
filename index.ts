

// function printInfo(labelInfo:{label:string}):string {
//     return labelInfo.label;
// }

// alert(printInfo({label:'123'}));

// interface FullName{
//     fistName:string;
//     lastName:string;
// }

// function printName(name:FullName) {
//     console.log(name.fistName + name.lastName);
// }

// printName({fistName:'123',lastName:'456'});

// interface FullName{
//     fistName:string;
//     lastName:string;
// }

// function printName(name:FullName) {
//     console.log(name.fistName + name.lastName);
// }
// printName({fistName:'周华建',lastName:'123'});

// interface FullName{
//     fistName:string;
//     lastName:string;
// }

// function printName(name:FullName) {
//     console.log(name.fistName + name.lastName);

// }
// printName({fistName:'呀呀',lastName:'呢哟'});

interface FullName{
    fistName?:string;
    lastName:string;
}

function printName(name:FullName) {
    console.log(name.fistName + name.lastName);
}

printName({lastName:'123'});










