
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
