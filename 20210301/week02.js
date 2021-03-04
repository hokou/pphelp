// 要求一:函式與流程控制
console.log("== 01 ==")

function calculate(min, max){
    // 請用你的程式補完這個函式的區塊 
    let total = 0;
    for (let i = min; i <= max; i++) {
        total = total + i
    }
    console.log(total);
}

calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30


// 要求二:Python 字典與列表、JavaScript 物件與陣列
console.log("== 02 ==")

function avg(data){
    // 請用你的程式補完這個函式的區塊 
    let num = data["count"];
    let total = 0;
    let salary = 0;
    for (let i = 0; i<data["employees"].length; i++) {
        salary = data["employees"][i]["salary"];
        total = total + salary;
    }
    let avg = total / num;
    console.log(avg);
}

avg({
"count":3,
"employees":[ {
"salary":30000 },
{
"name":"Bob",
"salary":60000 },
{
"name":"Jenny",
"salary":50000 }
]
});// 呼叫 avg 函式


// 要求三:演算法
console.log("== 03 ==")

function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊 
    if (nums.length>=2){
        let ans = nums[0]*nums[1];
        for (let i=0;i<nums.length;i++) {
            if (i <nums.length-1){
                for (let j=i+1;j<nums.length;j++) {
                    let check = nums[i]*nums[j];
                    if (check >= ans){
                        ans = check;
                    }
                }
            }
        }
        console.log(ans);
    } else {
        console.log("error, length must >= 2");
    }
}

maxProduct([5, 20, 2, 6]);// 得到 120 因為 20 和 6 相乘得到最大值 
maxProduct([10, -20, 0, 3]); // 得到 30 因為 10 和 3 相乘得到最大值
maxProduct([-10, 2]);


// 要求四 ( 請閱讀英文 ):演算法
console.log("== 04 ==")

function twoSum(nums, target){
    // your code here
    let ans = [0,0];
    for (let i=0;i<nums.length;i++){
        for (let j=i+1;j<nums.length;j++){
            let check = nums[i] + nums[j];
            // console.log(check)
            if (check == target){
                ans = [i, j];
                return ans
            } 
        }
    }
    return "no ans"
}

result=twoSum([2, 11, 7, 15], 9)
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


// 要求五 ( Optional ):演算法
console.log("== 05 ==")

function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊 
    let zeros_len = 0;
    let max_len = 0;
    for (let i=0;i<nums.length;i++) {
        if(nums[i]==0) {
            zeros_len++;
            for (let j=i+1;j<nums.length;j++) {
                if (nums[j] == 0){
                    // console.log(i,j);
                    zeros_len++;
                    if (zeros_len>max_len){
                        max_len = zeros_len;
                    }
                } else {
                    zeros_len = 0;
                    break;
                }
            }
        } else {
            continue;
        }
    }
    console.log(max_len)
}

maxZeros([0, 1, 0, 0]) // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) // 得到 4 
maxZeros([1, 1, 1, 1, 1]) // 得到 0


console.log("== 05-2 ==")

function maxZeros2(nums){
    // 請用你的程式補完這個函式的區塊 
    let zeros_len = 0;
    let max_len = 0;
    for (let i=0;i<nums.length;i++) {
        if(nums[i]==0) {
            zeros_len++;
            if (zeros_len>max_len){
                max_len = zeros_len;
            }
        } else {
            zeros_len = 0;
            continue;
        }
    }
    console.log(max_len)
}

maxZeros2([0, 1, 0, 0]) // 得到 2
maxZeros2([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) // 得到 4 
maxZeros2([1, 1, 1, 1, 1]) // 得到 0
