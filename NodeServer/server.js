const express = require('express'); 
var bodyParser = require('body-parser')
const app = express(); 
const port = 8080; 
const http = require('http').Server(app)
var mongoose = require('mongoose')
var fs = require('fs-extra')
const multer = require("multer");
app.use(express.static(__dirname+"/static"))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))

var dbUrl= 'mongodb+srv://luuvanduc:poiu1234@chathear.zkuk0.mongodb.net/chathear?retryWrites=true&w=majority'

var storage = multer.diskStorage(
    {
        destination: (req, file, callback) => {
            let type = req.body.dir;
            let path = `./upload/${type}`;
            fs.mkdirsSync(path);
            callback(null, path);
          },
        filename: function ( req, file, cb ) {
            //req.body is empty...
            //How could I get the new_file_name property sent from client here?
            cb( null, file.originalname);
        }
    }
);

var upload = multer( { storage: storage } );

app.post("/upload", upload.array("files"), uploadFiles);

function uploadFiles(req, res) {
    console.log(req.body.name);
    console.log(req.files);
    res.json({ message: "Successfully uploaded files" });
}



mongoose.connect(dbUrl,{ useNewUrlParser: true, useUnifiedTopology: true }, (err)=>{
    console.log("err:", err)
})

var server = http.listen(port, ()=>{
    console.log("listening port", server.address().port)
})