
  function msg(){
  document.getElementById("succ").innerHTML = "Sie wollen Snack succen? Oben links? OK.";
  $.ajax({
    url: "/etc/www/html/test.py",
    context: document.body}).done(function(){
    alert('finished');
    });
  }


