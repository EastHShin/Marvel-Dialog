function suggestion() {
    var textarea = document.getElementById("context");
    var context = textarea.value;

    var models = document.getElementById("model");
    var model = models.options[models.selectedIndex].value;




    var formData = new FormData();
    formData.append("context", context );
    formData.append("model", model);

    fetch(
        "/gpt2",
        {
            method: "POST",
            body:formData
        }
    )
    .then(response => {
        if (response.status == 200){
            return response
        }
        else{
            throw Error("Failed");
        }
    })
    .then(response => response.json())
    .then(response => {
        var items = document.getElementsByClassName("item");

        for (let index = 0; index < response[0].length; index++) {

            if(response[0][index][0]) {
                items[index].innerHTML = response[0][index][0];
                items[index].innerHTML += " : ";
                items[index].innerHTML += response[0][index][1];
            }
            else
                items[index].innerHTML = ""
        }

    })
    .catch(e => {
        var item = document.getElementsByClassName("item")[0];
        item.innerHTML=e;
    })
}

