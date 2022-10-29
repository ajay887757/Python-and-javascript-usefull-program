// let userData={
//     "user1" : {
//        "name" : "mahesh",
//        "password" : "password1",
//        "profession" : "teacher",
//        "id": 1
//     },
    
//     "user2" : {
//        "name" : "suresh",
//        "password" : "password2",
//        "profession" : "librarian",
//        "id": 2
//     },
    
//     "user3" : {
//        "name" : "ramesh",
//        "password" : "password3",
//        "profession" : "clerk",
//        "id": 3
//     }
// }

var express = require('http');
const server =http.createServer((req,res)=>{
    if (req.url="/"){
        console.log("Hello World")
    }
})

server.listen(8000,"127.0.0.1",()=>{
    console.log("Hello ")
})