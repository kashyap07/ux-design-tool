
    var startTime = new Date();  
    h = (startTime.getHours()<10?'0':'') + startTime.getHours(),
    m = (startTime.getMinutes()<10?'0':'') + startTime.getMinutes();
    var st=h + ':' + m  ;    
    window.onbeforeunload = function()        
    {
        var endTime = new Date(); 
        h2 = (endTime.getHours()<10?'0':'') + endTime.getHours(),
        m2 = (endTime.getMinutes()<10?'0':'') + endTime.getMinutes();
        var et=h2 + ':' + m2 ;      
        var timeSpent = JSON.stringify({"from":st,"to":et});
        
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
