var api_base_url = "http://127.0.0.1:8000/api/";

let button = document.getElementById("btnSaveEvent");
button.addEventListener("click", create_task);

function create_task(params) {
    let token = getCookie("XSRF-TOKEN");

    let AddTitle = document.getElementById("AddTitle");
    let restrictionAddDescriptions = document.getElementById("restrictionAddDescriptions");
    let restrictionaddDate = document.getElementById("restrictionaddDate");
    let expectedTime = document.getElementById("expectedTime");
    let payload = {
        "title": AddTitle.value,
        "description": restrictionAddDescriptions.value,
        "dead_line": restrictionaddDate.value,
        "expected_time": expectedTime.value
    }
    
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            window.location.replace("/home");
        }
        else
        {   
            console.log(payload);
            console.log(token);
            console.log("Response status:" + xhttp.status)
            console.log("Response error:" + xhttp.responseText)
            alert("Falha ao criar a tarefa! Por favor, tente novamente.")
        }
    };
    xhttp.open("POST", api_base_url + "tasks/create");
    xhttp.setRequestHeader("Authorization", token);
    xhttp.setRequestHeader("Content-type", "application/json");
    
    xhttp.send(JSON.stringify(payload));
}

function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }