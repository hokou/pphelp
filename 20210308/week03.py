import urllib.request
import json, ssl

context = ssl._create_unverified_context()

try:
    url = "https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"
    print("origin-1")
    with urllib.request.urlopen(url, context=context) as jsondata:
        data_json = json.loads(jsondata.read().decode())

except:
    url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
    print("origin-2")
    with urllib.request.urlopen(url, context=context) as jsondata:
        data_json = json.loads(jsondata.read().decode())

data = data_json["result"]["results"]

data_txt = 'data.txt'
with open(data_txt,"w",encoding="utf-8") as f:
    for i in range(len(data)):
        img = data[i]["file"]
        img = img.split("http://")
        # print(img)
        img = img[1].replace("www","http://www")
        temp = data[i]["stitle"] + "," + data[i]["longitude"] + "," + data[i]["latitude"] + "," + img + "\n"
        f.write(temp)


# data.txt 的資料格式
# 景點名稱,經度,緯度,第一張圖檔網址
# 景點名稱,經度,緯度,第一張圖檔網址
