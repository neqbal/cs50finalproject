function like(clicked_id) {
  document.getElementById(clicked_id).style.display="none";
  document.getElementById("dislike" + clicked_id.slice(4)).style.display="block";
}
  
function dislike(clicked_id) {
  document.getElementById("like" + clicked_id.slice(7)).style.display="block";
  document.getElementById(clicked_id).style.display="none";
}



