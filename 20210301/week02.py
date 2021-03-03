# 要求一:函式與流程控制
print("== 01 ==")

def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    total = 0
    for i in range(min,max +1):
        total = total + i
    print(total)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


# 要求二:Python 字典與列表、JavaScript 物件與陣列
print("== 02 ==")

def avg(data):
    # 請用你的程式補完這個函式的區塊
    num = data["count"]
    total = 0
    for i in range(len(data["employees"])):
        salary = data["employees"][i]["salary"]
        total = total + salary
    avg = total / num
    print(avg)

avg({
    "count":3, 
    "employees":[
        {
        "name":"John",
        "salary":30000 },
        {
        "name":"Bob",
        "salary":60000 },
        {
        "name":"Jenny",
        "salary":50000 }
        ]
}) # 呼叫 avg 函式


# 要求三:演算法
print("== 03 ==")

def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    ans = 0
    for i in range(len(nums)):
        if i < len(nums)-1:
            for j in range(i+1,len(nums)):
                # print(i,j,":",nums[i],nums[j])
                check = nums[i]*nums[j]
                if check >= ans:
                    ans = check
                # print(check,ans)
    print(ans)

maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值 
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值


# 要求四 ( 請閱讀英文 ):演算法
print("== 04 ==")

def twoSum(nums, target):
    # your code here
    ans = [0,0]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            # print(i,j,nums[i],nums[j])
            check = nums[i]+nums[j]
            # print(check)
            if check == target:
                ans = [i,j]
                return ans
    
    return "no ans"


result = twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


# 要求五 ( Optional ):演算法
print("== 05 ==")

def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    zeros_len = 0
    max_len = zeros_len
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros_len += 1
            for j in range(i+1,len(nums)):
                if nums[j] == 0:
                    # print(i,j,nums[i],nums[j])
                    zeros_len += 1
                    # print(zeros_len)
                    if zeros_len > max_len:
                        max_len = zeros_len
                        # print(zeros_len,max_len)
                else:
                    zeros_len = 0
                    break
        else:
            continue

    print(max_len)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0