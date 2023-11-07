function like(clicked_id) {
  const xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://127.0.0.1:5000/liked_data?post_id=" + clicked_id);
  xhttp.send();
  xhttp.onreadystatechange = (e) => {
    let res = xhttp.responseText;
    
    if (res.slice(0,4) === "like") {
      document.getElementById("like" + clicked_id).style.display = "none";
      document.getElementById("dislike" + clicked_id).style.display = "block";
      document.getElementById("count" + clicked_id).innerHTML=res.slice(4);
    }
    else {
      document.getElementById("like" + clicked_id).style.display = "block";
      document.getElementById("dislike" + clicked_id).style.display = "none";
      document.getElementById("count" + clicked_id).innerHTML=res.slice(7);
    }
  }
}