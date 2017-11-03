

var express = require('express');
var app     = express();
var server  = app.listen(21);
var bodyParser = require('body-parser');


var stdin = process.openStdin();
 

//app.get('/output', function(request, response) {
 // response.send(  d );
//});


app.use(bodyParser.urlencoded({ extended: true }));

app.post('/myaction', function(req, res) {
  //res.send('You sent the name "' + req.body.name + '".');
  //res.send(' synonms: ' + req.body.name + ' .');




var spawn = require('child_process').spawn,
    py    = spawn('python', ['synoymn.py']),
    
    data =   req.body.name,
    dataString = '';
	py.stdin.write(data)  ;
	py.stdin.end();

	py.stdout.on('data', function(data){
	dataString += data.toString();
	//console.log('Sum  ', dataString  );
}); 




py.stdout.on('end', function(){
  console.log( dataString );
  d=dataString
  res.send('interchanged synonms: ' + d + ' .');
 


});

//the interchanged synonm
 

});








