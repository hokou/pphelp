
const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json";

fetch(url).then(function(response){
    return response.json();
}).then(function(result){
    result = result.result.results;
    // console.log(result);
    // return result;
    let list=document.querySelector("#row");
    let ori_length = 0;
    let add_length = 8;
    render(list,ori_length,add_length,result);
});

function render(list,ori_length,add_length,result){
    for (let i=ori_length;i<ori_length+add_length;i++){
        // console.log(result[i].stitle);
        let title = result[i].stitle;
        let img = result[i].file.split("http");
        img = "http" + img[1];
        // console.log(img);
        let div_block = document.createElement("div");
        let div_title = document.createElement("div");
        let div_img = document.createElement("div");
        div_block.className="block";
        div_title.className="title";
        div_img.className="pic";
        div_title.textContent=title;
        div_img.style.backgroundImage="url(" + img + ")";
        // console.log('"url(' +img +')"');
        list.appendChild(div_block);
        div_block.appendChild(div_img);
        div_block.appendChild(div_title);
    }
}



