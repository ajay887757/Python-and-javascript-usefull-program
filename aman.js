var readline = require('readline');

var rl = readline.createInterface(process.stdin, process.stdout);
// rl.question('What is 1+1 ', (question1) => {
//     console.log('What is 1+1 ');
//     console.log('A: ' + "2");
//     console.log('B: ' + "3");
//     console.log('C: ' + "4");
//     console.log('D: ' + 1);
//     console.log('E: ' + 5);
// });

var AllQuestion={"what is 1+1":[2,3,4,5,1],"what is 10+20":[10,30,40,50,20]}
correctAnswer={1:2,2:30}
options=["A","B","C","D","E"]

async function test(){

for( let x in AllQuestion) {
    console.log(x)
    let i=0
    await AllQuestion[x].forEach(element => {
        console.log(options[i],element)
        i++
    });
    id=false
    rl.question('Enter Option', (option) => {
        console.log("Next",option)
    })
}
}

test()
