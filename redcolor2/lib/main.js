var OERF_JSON = "http://www.oref.org.il/WarningMessages/alerts.json";
var OERF_JSON1 = "http://cucomania.mooo.com/alerts.json";
var tmr = require('sdk/timers');
var lastNotificationTime = -1;


tmr.setInterval(checkStatus, 2000);
checkStatus();


function checkStatus(){
    const {XMLHttpRequest} = require("sdk/net/xhr");
    var request = new XMLHttpRequest();
    request.open("GET", OERF_JSON, true);
    request.overrideMimeType('text/plain; charset=UTF-16'); 
    request.onload = function () {
        // console.log(request.responseText);
        var jsonResponse = JSON.parse(request.responseText);
        if (jsonResponse.data.length>0 && lastNotificationTime!=jsonResponse.id) {
            lastNotificationTime = jsonResponse.id;
            showRedColor(jsonResponse.title, jsonResponse.data.join(", "));
        }
    };
    request.send();
}

function showRedColor(theTitle, where) {
	var notifications = require("sdk/notifications");
    // notifications.
	notifications.notify({
	  title: theTitle,
	  text: where,
	  onClick: function () {
	    //console.log(data);
	    // console.log(this.data) would produce the same result.
	  }
	});
}
