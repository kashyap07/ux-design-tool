	<script>
	var startTime=new Date().getTime();
  var endTime=new Date().getTime();
	window.onscroll=senddet;
	
    function senddet()
    {
      window.onscroll=senddet2;
    }
    function senddet2()
    {
      endTime = new Date().getTime();
    	var diff=endTime-startTime;
    	if (diff > 60000)//1 minute as ameasure now
    	{
    	if(document.body.scrollTop)
    		var sc=document.body.scrollTop;
    	else
    		var sc=document.documentElement.scrollTop;
      var timeSpent = JSON.stringify({"position":sc,"timeSpent":diff});
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/send3", true);
      xhr.setRequestHeader("Content-type", "application/json");
      xhr.send(timeSpent);
      xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
      console.log("sending");}};
      startTime=new Date().getTime();
      }
    }

</script>