<script type="text/javascript">
    var startTime = new Date();        
    window.onbeforeunload = function()        
    {
        var endTime = new Date();        
        var timeSpent = JSON.stringify({"from":startTime,"to":endTime});
        var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    console.log("sending");
    }
    };
    xhr.open("POST", "/send2", true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.send(timeSpent);
    }
</script>