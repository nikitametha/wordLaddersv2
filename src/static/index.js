// Functionality for 'How to Play' button

var helpmodal = document.getElementById("helpModal");
// Get the button that opens the modal
var abtbtn = document.getElementById("about");

// Get the <span> element that closes the modal
var abtspan = document.getElementById("close-modal");

// When the user clicks on the button, open the modal
abtbtn.onclick = function() {
  helpmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
abtspan.onclick = function() {
  helpmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    helpmodal.style.display = "none";
  }
}


// Functionality for 'word ladder solver' button
var solvermodal = document.getElementById("solverForm");
var solverbtn = document.getElementById("solver");

// Get the <span> element that closes the modal
var solverspan = document.getElementById("close-solverform");

// When the user clicks on the button, open the modal
solverbtn.onclick = function() {
  solvermodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
solverspan.onclick = function() {
  solvermodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == solvermodal) {
    solvermodal.style.display = "none";
  }
}


// Functionality for 'play the game' button

var playmodal = document.getElementById("playModal");
// Get the button that opens the modal
var playbtn = document.getElementById("playgame");

// Get the <span> element that closes the modal
var playspan = document.getElementById("close-playmodal");

// When the user clicks on the button, open the modal
playbtn.onclick = function() {
  playmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
playspan.onclick = function() {
  playmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    playmodal.style.display = "none";
  }
}



/*
function hardlvl()
{
 inter={{leng}};  
 lst2="{{ll}}";
  lst=lst2.split(" ");
  neww=1;
  //alert(lst[0]);
  //alert(lst[1]);
  //alert(lst[inter-1]);
  var div1=document.createElement("div");
  div1.id="divv1";
  div1.className="divs";
  div1.style.border="1px solid black";

  var p1=document.createElement("p");
  p1.className="paras";
  p1.innerHTML="START WORD: "+ "{{x[0]}}";

  var p2=document.createElement("p");
  p2.className="paras";
  p2.innerHTML="END WORD: "+"{{x[1]}}";
  div1.appendChild(p1);
  div1.appendChild(p2);
  document.body.appendChild(div1);

  var div2=document.createElement("div");
  div2.id="divv2";
  var p3=document.createElement("p");
  var inp=document.createElement("input");
  p3.className="para";
  p3.innerHTML="MAKE THE WORD BRIDGE!";
  inp.type="text";
  inp.id="inputts";
  inp.placeholder="Guess the next word!";
  var chec=document.createElement("input");
   chec.className="chc";
  chec.type="button";
  chec.value="Check";
  chec.onclick=checkk;

var gp=document.createElement("input");
  gp.type="button";
  gp.className="chc2";
  gp.value="GIVE UP";
  gp.onclick=giveup;

  var hintbut=document.createElement("p");
  hintbut.id="hin";
  hintbut.className="hintt";
  hintbut.innerHTML="HINT:";
  hintbut.style.border="1px solid black";
  div2.appendChild(p3);
   div2.appendChild(inp);
div2.appendChild(chec);
div2.appendChild(hintbut);
div2.appendChild(gp);
document.body.appendChild(div2);
}

function giveup()
{  var hintbut=document.getElementById("hin");
  var div2=document.getElementById("divv2");

 while(neww<inter)
   { 

    var linked=document.createElement("p");
      linked.className="links";	
      linked.innerHTML=lst[neww];
      div2.appendChild(linked);
      neww=neww+1;
   }
   var playagain=document.createElement("input");
   playagain.type="button";
   playagain.className="chc2";
   playagain.value="PLAY AGAIN!";
   playagain.onclick=reloadd; 
   div2.appendChild(playagain);
}

 function checkk()
{ var c= document.getElementById("inputts").value;
  //alert(c);
//alert(lst[neww]);
  var hintbut=document.getElementById("hin");
  var div2=document.getElementById("divv2");
  if((c==lst[inter-1])&&(neww==inter-1))
 { alert("YOU HAVE WON!");
   var playagain=document.createElement("input");
   playagain.type="button";
   playagain.value="PLAY AGAIN!";
   playagain.onclick=reloadd; 
   div2.appendChild(playagain);
   }
  if(c==lst[neww])
    { var linked=document.createElement("p");
      linked.className="links";
      linked.innerHTML=c;
      neww=neww+1;
      hintbut.innerHTML="You have guessed right! ";
      div2.appendChild(linked);}
  else

      if((lst[neww-1].length)<(lst[neww].length))
			{ hintbut.innerHTML="HINT: Try again! Add a letter!";}
  else
   if((lst[neww-1].length)>(lst[neww].length))
			{ hintbut.innerHTML="HINT: Try again! Delete a letter!";}
    else
			{ hintbut.innerHTML="HINT: Try again! Change a letter!";}
      
     
 
}


*/
