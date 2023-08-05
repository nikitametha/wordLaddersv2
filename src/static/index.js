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
  if (event.target == playmodal) {
    playmodal.style.display = "none";
  }
}
