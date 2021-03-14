
const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json";

// 起始值
// 第一次顯示數量
// 結束值
let ori_length = 0;
let first_num = 8;
let end_length = ori_length + first_num;

// 按一次增加的數量
// JSON 總數量
let oneclick_num = 8;
let total_length = 0;
// total = 319


function fetch_url(){
    fetch(url).then(function(response){
        return response.json();
    }).then(function(result){
        result = result.result.results;
        total_length = result.length;
        let list = document.querySelector("#row");
        if (end_length >= total_length){
            end_length = total_length;
        };
        // console.log("add,tot",end_length,total_length);
        // console.log(result);
        render(list,ori_length,end_length,result);
    });
};



function render(list,ori_length,end_length,result){
    for (let i=ori_length;i<end_length;i++){
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
        list.appendChild(div_block);
        div_block.appendChild(div_img);
        div_block.appendChild(div_title);
    }
    // console.log(ori_length,end_length);
}


function loadmore() {
    ori_length = end_length;
    end_length += oneclick_num;
    // console.log("loadmore",ori_length,end_length,oneclick_num);
    fetch_url();
}

fetch_url();