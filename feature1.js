<script>
if (document.addEventListener) {
    document.getElementsByTagName("body")[0].addEventListener("click", addclickpt);
} else if (document.attachEvent) {
    document.getElementsByTagName("body")[0].attachEvent("onclick", addclickpt);
}
function addclickpt()
{
	var x = event.clientX;
    var y = event.clientY;
    var d = new Date();
	var t=d.getHours()+":"+d.getMinutes()+":"+d.getSeconds();
    var coords = JSON.stringify({"x":x,"y":y,"time":t});

    //send the coords to the server for database updates

    var xhr = new XMLHttpRequest();
  	xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    console.log("sending");
    }
  	};
  	xhr.open("POST", "/send1", true);
  	xhr.setRequestHeader("Content-type", "application/json");
  	xhr.send(coords);
}
</script>