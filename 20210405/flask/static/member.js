
// 查詢使用者姓名
function fetch_namequery(){
    let name_query = document.querySelector("#name_query");
    const namequery_api = `http://127.0.0.1:3000/api/users?username=${name_query.value}`
    fetch(namequery_api).then(function(response){
        return response.json();
    }).then(function(result){
        // console.log(result);
        let nameans = document.querySelector("#nameans");
        if (result.data!=null){
            result = result.data;
            nameans.innerText=result.name+`(${name_query.value})`;
        }else {
            nameans.innerText="查詢失敗";
        }
        // name_query.value = "";
    })
}

// 更改姓名
function fetch_rename(){
    let name_change = document.querySelector("#name_change");
    const rename_api = 'http://127.0.0.1:3000/api/user';
    let rename_json = {
        "name":name_change.value
        };
    fetch(rename_api, {
        method:'POST',
        body:JSON.stringify(rename_json),
        headers: {
            'Content-Type': 'application/json'
          }
    }).then(function(response){
        return response.json();
    }).then(function(result){
        console.log(result);
        let renameans = document.querySelector("#renameans");
        let name = document.querySelector("#name");
        if (result.ok == true){
            renameans.innerText = "更新成功";
            name.innerText = name_change.value
        } else {
            renameans.innerText = "更新失敗";
        }
    }).catch(function() {
        renameans.innerText = "更新失敗，再試一次";
    })
}