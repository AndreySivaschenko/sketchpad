function check_event() {
  	Data = new Date();
	Hour = Data.getHours();
	Minutes = Data.getMinutes();
	var time = Hour + ":" + Minutes;
	alert(time);
	$.ajax({
   	url: "/user/check_event/",
	   method:"GET",
	   data:{
		    'notes_time': time
	   },
	   cache:false,
	   dataType:"text",
	   success : function (data) {
		   if(data == 'yes'){
		   	alert("У вас запланированно дело!");
		   }
		   else if(data == 'no'){
		   	alert("no");
		   }
       }
   });
}

window.onload = function () {
    check_event();
    setInterval(check_event,60000);
};

