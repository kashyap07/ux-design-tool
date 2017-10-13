if (document.addEventListener) 
{
    document.getElementsByTagName("body")[0].addEventListener("click", addclickpt);
} 
else if (document.attachEvent) 
{
    document.getElementsByTagName("body")[0].attachEvent("onclick", addclickpt);
}

function addclickpt()
{
	var x = event.clientX;
    var y = event.clientY;
	var t = new Date().toISOString();
    var type = "click"
    var coords = JSON.stringify({"x" : x, "y" : y, "time" : t, "type" : type});

    //send the coords to the server for database updates

    var xhr = new XMLHttpRequest();
  	xhr.onreadystatechange = function() {
    	if (this.readyState == 4 && this.status == 200) 
    	{
    		console.log("sent");
    	}
  	};

  	var form = new FormData();
  	form.append("data", coords);
  	xhr.open("POST", "http://localhost/store:8888", true);
  	xhr.send(form);
}
