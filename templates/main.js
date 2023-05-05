// Onclick of the button
document.getElementById("testButton1").onclick = function () {  
  // Call python's random_python function
  eel.random_python()(function(number){                      
    // Update the div with a random number returned by python
    document.getElementById("number").innerHTML = number;
  })
}