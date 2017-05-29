$(document).ready(function(){
$("#msg_event_close").click(function () {
var date = new Date();
date.setTime(date.getTime() + (60 * 60000));
$.cookie("msg", "", {expires: date} );
$("#msg_pop").hide();
});

if ( $.cookie("msg") == null )
{
setTimeout(function(){
$("#msg_pop").show();
}, 4000)
}
else { $("#msg_pop").hide();
}
});

