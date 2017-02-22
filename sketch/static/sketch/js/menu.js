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

window.onload = function(){
	openMenu();
	priority();
};