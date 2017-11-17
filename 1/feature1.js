if (document.addEventListener) {
    document.getElementsByTagName("body")[0].addEventListener("click", addclickpt);
} else if (document.attachEvent) {
    document.getElementsByTagName("body")[0].attachEvent("onclick", addclickpt);
}
function addclickpt(event)
{
	  var x = event.clientX;
    var y = event.clientY;
    var d = new Date();
    h = (d.getHours()<10?'0':'') + d.getHours(),
    m = (d.getMinutes()<10?'0':'') + d.getMinutes();
    var t=h + ':' + m
    var coords = JSON.stringify({"x":x,"y":y,"time":t});
    //send the coords to the server for database updates
    //console.log(t);
    var xhr = new XMLHttpRequest();
  	xhr.onreadystatechange = function() 
    {
    if (this.readyState == 4 && this.status == 200) 
      {
        console.log("sending");
      }
  	};
  	xhr.open("POST", "http://127.0.0.1:5000/send", true);
  	xhr.setRequestHeader("Content-type", "application/json");
  	xhr.send(coords);
    //console.log("sending");
}
