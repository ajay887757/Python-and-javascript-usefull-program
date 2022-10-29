// var listData=[2,4,6,8,10,12]
var listData=[2,4,6,8,10]

var newList=[]

lenData=listData.length/2
console.log(typeof(lenData));


// console.log(Math.floor(lenData));
j=listData.length-1
for (let i=0;i<lenData;i++){
    console.log(i)
    if (listData[j]==listData[i]){
        newList.push(listData[j]) 
    }
    else{
    newList.push(listData[j])
    newList.push(listData[i])
    }
    j=j-1
}

console.log(newList)