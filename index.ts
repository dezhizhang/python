

interface encrypt{
    (key:string,value:string):string;
}

let md5:encrypt = function(key:string,value:string):string{
    return key+value;
}

console.log(md5('name','123'));















