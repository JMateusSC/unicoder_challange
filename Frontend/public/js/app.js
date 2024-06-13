var api_base_url = "http://127.0.0.1:8000/api/";

let button = document.getElementById("btnSaveEvent");
button.addEventListener("click", create_task);

function create_task(params) {
    let token = document.cookie["auth_token"];

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