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
	var arrowNext = document.getElementById('ar-next');
	var date = document.getElementsByClassName("date-row");
	var note = document.getElementsByClassName('note-row');
	arrowPrew.style.display = 'none';

	arrowNext.onclick = function () {
		for(var i = 0; i < date.length; i++){
			if(i == 0){
				date[i].style.display = "none";
			} else if(i == 1){
				date[i].style.display = "none";

			}

			if(i == 5 && date[i].style.display != "block"){
				date[i].style.display = "block";
			}else if(i == 6 && date[i].style.display != "block" ){
				date[i].style.display = "block";
				arrowNext.style.display = 'none';
				arrowPrew.style.display = "block";

			}
		}
    };
	arrowPrew.onclick = function () {
		for(var i = 0; i < date.length; i++){
			if(i == 0 ){
				date[i].style.display = "block";
			} else if(i == 1){
				date[i].style.display = "block";
			}

			if(i == 5 && date[i].style.display == "block"){
				date[i].style.display = "none";
				note[i].style.display = "none";
			}else if(i == 6 && date[i].style.display == "block"){
				date[i].style.display = "none";
				note[i].style.display = "none";
				arrowNext.style.display = 'block';
				arrowPrew.style.display = "none";
			}
		}
    };
}



window.onload = function(){
	openMenu();
	priority();
	hideDateNav();
	sellectArrow();
};