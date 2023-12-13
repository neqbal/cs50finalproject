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

function del(clicked_id) {
  const xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://127.0.0.1:5000/delete?id=" + clicked_id);
  xhttp.send();
  xhttp.onreadystatechange = (e) => {
    let res=xhttp.responseText;

    if(res === "delete") {
      if(clicked_id.slice(0,3) === "cmt") {
        console.log(clicked_id.slice(0,3));
        window.location.replace("http://127.0.0.1:5000/myprofile?myprofile=" + "comments" );
      }
      else {
        window.location.replace("http://127.0.0.1:5000/myprofile?myprofile=" + "myposts");
      }
    }
  }
}


function view(clicked_id) {
  if (clicked_id === "Column") {
    document.getElementById("middle-container").style.flexDirection="column";
    console.log(clicked_id); 
  }
  else {
    document.getElementById("middle-container").style.flexDirection="row";
    console.log(clicked_id);
  }
}