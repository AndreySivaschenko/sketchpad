function filt() {
    var pr = document.querySelectorAll('#prior');
    var Priority = document.querySelectorAll(".note");

    var chbox;
    var chbox_1;
    var chbox_2;
    var chbox_3;
    chbox = document.getElementById("inlineCheckbox1");
    chbox_1 = document.getElementById("inlineCheckbox2");
    chbox_2 = document.getElementById("inlineCheckbox3");
    chbox_3 = document.getElementById("inlineCheckbox4");
    var mainMenu;
    mainMenu = document.getElementById("mainMenu");
    function foo(){alert("Hi");}

    mainMenu.addEventListener("click", foo());


}

window.onload = function(){
  filt();
};