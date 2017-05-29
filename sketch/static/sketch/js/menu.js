function openMenu(){
	var btnOpenMenu = document.getElementById("open");
		mask = document.getElementById("mask");
		menu = document.getElementById("menu");

	menu.style.display = 'none';
	mask.style.display = "none";

	btnOpenMenu.onclick = function(){
		menu.style.display = "block";
		mask.style.display = "block";
	};

	mask.onclick = function(){
		menu.style.display = "none";
		mask.style.display = "none";
	};
}
function priority() {
	var pr = document.querySelectorAll('#prior');
	var Priority = document.querySelectorAll(".note");
	for(var i = 0; i < Priority.length; i++){
		if(typeof pr[i] !== 'undefined' && pr[i] !== null) {
            switch (pr[i].value) {
                case "0":
                    Priority[i].style.borderLeft = "5px solid #9b9b9b";
                    break;
                case "1":
                    Priority[i].style.borderLeft = "5px solid #00ff60";
                    break;
                case "2":
                    Priority[i].style.borderLeft = "5px solid #f6ff00";
                    break;
                case "3":
                    Priority[i].style.borderLeft = "5px solid #f34747";
                    break;
            }
        }
	}

}

function hideDateNav() {
	var date = document.getElementsByClassName("date-row");
	for(var i = 0; i < date.length; i++){
		if(i == 5){
			date[i].style.display = "none";
		}else if(i == 6){
			date[i].style.display = "none";
		}
	}
}

function sellectArrow() {
	var arrowPrew = document.getElementById("ar-prev");
	var	arrowNext = document.getElementById("ar-next");
	var	date = document.getElementsByClassName("date-row");
	var note_1 = document.getElementById('notes_1');
	var note_2 = document.getElementById('notes_2');
	var note_6 = document.getElementById('notes_6');
	var note_7 = document.getElementById('notes_7');

	arrowPrew.style.display = 'none';

	arrowNext.onclick = function () {
		for(var i = 0; i < date.length; i++){
			if(i == 0){
				date[i].style.display = "none";
				note_1.style.display = "none";
			} else if(i == 1){
				date[i].style.display = "none";
				note_2.style.display = "none";
			}

			if(i == 5){
				date[i].style.display = "block";
				note_6.style.display = "block";
			}else if(i == 6 ){
				date[i].style.display = "block";
				note_7.style.display = "block";

				arrowNext.style.display = 'none';
				arrowPrew.style.display = "block";

			}
		}
    };

	arrowPrew.onclick = function () {
		for(var i = 0; i < date.length; i++){
			if(i == 0 ){
				date[i].style.display = "block";
				note_1.style.display = "block";
			} else if(i == 1){
				date[i].style.display = "block";
				note_2.style.display = "block";
			}

			if(i == 5){
				date[i].style.display = "none";
				note_6.style.display = "none";
			}else if(i == 6){
				date[i].style.display = "none";
				note_7.style.display = "none";

				arrowPrew.style.display = "none";
				arrowNext.style.display = 'block';

			}
		}
    };
}


function optionNote(){
	var btnEdit = document.getElementById('m-edit'),
		btnDelete = document.getElementById('m-delete'),
		done = document.getElementsByClassName("done"),
		note = document.querySelectorAll(".note"),
		edit = document.getElementsByClassName("edit"),
		deletes = document.getElementsByClassName("delete");

	btnEdit.onclick = function(){
		for(var i = 0; i < note.length; i++){
				done[i].style.display = 'none';
				deletes[i].style.display = 'none';
    	        edit[i].style.display = "block";
			}
		};

		btnDelete.onclick = function(){
		for(var i = 0; i < note.length; i++){
				done[i].style.display = 'none';
				edit[i].style.display = 'none';
				deletes[i].style.display = "block";
			}
		};

}

function check_event() {
  	Data = new Date();
  	Year = Data.getFullYear();
	Month = Data.getMonth()+1;
	Day = Data.getDate();
	Hour = Data.getHours();
	Minutes = Data.getMinutes();
  	if (Day < 10) Day = '0' + Day;
	if (Month < 10) Month = '0' + Month;
	var time = Hour + ":" + Minutes;
	var date = Year + "-" + Month + "-" + Day;
	$.ajax({
   	url: "/user/check_event/",
	   method:"GET",
	   data:{
		    'notes_time': time,
		   	'notes_date':date
	   },
	   cache:false,
	   dataType:"text",
	   success : function (data) {
		   if(data == 'yes'){

		   	var event_pop = document.getElementById('event_pop');
        	setTimeout("document.getElementById('event_pop').style.display='block'; document.getElementById('event_pop').className += 'fadeIn';audio.play();");

		   }
       }
   });
}

window.onload = function(){
	openMenu();
	priority();
	hideDateNav();
	sellectArrow();
	optionNote();
	check_event();
	scroll();
	setInterval(check_event,60000);
};