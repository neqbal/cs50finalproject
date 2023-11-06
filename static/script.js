function likecounter(url, post_id) {
  const xhttp = new XMLHttpRequest();
  xhttp.open("GET", url);
  xhttp.send();
  xhttp.onreadystatechange = (e) => {
    document.getElementById("count" + post_id).innerHTML = xhttp.responseText;
  }
}

function like(clicked_id) {
  document.getElementById(clicked_id).style.display="none";
  document.getElementById("dislike" + clicked_id.slice(4)).style.display="block";

  likecounter("http://127.0.0.1:5000/likes", clicked_id.slice(4));
}
  
function dislike(clicked_id) {
  document.getElementById("like" + clicked_id.slice(7)).style.display="block";
  document.getElementById(clicked_id).style.display="none";

  likecounter("http://127.0.0.1:5000/dislikes", clicked_id.slice(7));
}



