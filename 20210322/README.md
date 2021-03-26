## 要求一:安裝 MySQL 伺服器  

![1-1](/img/1-1.png)


## 要求二:建立資料庫和資料表  

- 建立一個新的資料庫，取名字為 website

```sql
CREATE DATABASE website;
```
![2-1](/img/2-1.png)

- 在資料庫中，建立資料表，取名字為user。資料表中必須包含以下欄位設定：

| 欄位名稱 | 資料型態     | 額外設定                   | 用途說明 |
| :------- | :----------- | :------------------------- | :------- |
| id       | bigint       | 主鍵、自動遞增             | 獨立編號 |
| name     | varchar(255) | 不可為空值                 | 姓名     |
| username | varchar(255) | 不可為空值                 | 帳戶名稱 |
| password | varchar(255) | 不可為空值                 | 帳戶密碼 |
| time     | datetime     | 不可為空值，預設為當前時間 | 註冊時間 |

```sql
use website;

CREATE TABLE user (
  id BIGINT AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  username varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  time datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
```
![2-2](/img/2-2.png)

## 要求三:基本的 SQL 指令

- 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和 password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。

```sql
INSERT INTO user (name, username, password)
  VALUES ("test1", "ply", "ply");
 
INSERT INTO user (name, username, password)
  VALUES
  ("test2", "apple", "apple"),
  ("test3", "pp", "pp"),
  ("test4", "schemas", "schemas"),
  ("test5", "food", "food");

-- 多筆時間會一樣
```
![3-1](/img/3-1.png)

- 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。

```sql
SELECT * FROM website.user;
```
![3-2](/img/3-2.png)

- 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。

```sql
SELECT COUNT(*) FROM website.user;
```
![3-3](/img/3-3.png)

- 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近到遠排序。

```sql
SELECT * FROM website.user
ORDER BY time DESC;
```
![3-4](/img/3-4.png)

- 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。

```sql
SELECT * FROM website.user
ORDER BY time DESC LIMIT 1,3;
```
![3-5](/img/3-5.png)

- 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。

```sql
SELECT * FROM website.user
WHERE username='ply';
```
![3-6](/img/3-6.png)

- 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。

```sql
SELECT * FROM website.user
WHERE username='ply' AND password='ply';
```
![3-7](/img/3-7.png)

- 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位改成【丁滿】。

```sql
SET SQL_SAFE_UPDATES=0;
UPDATE website.user SET name='丁滿' WHERE username='ply';
SET SQL_SAFE_UPDATES=1;
```
![3-8](/img/3-8.png)

- 使用 DELETE 指令刪除所有在 user 資料表中的資料。

```sql
DELETE FROM user;

DROP TABLE user;
-- 刪除資料表
```
![3-9](/img/3-9.png)


## 要求四:結合資料表 SQL JOIN 的操作 (Optional)

- 在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定:

| 欄位名稱 | 資料型態     | 額外設定                                | 用途說明     |
| :------- | :----------- | :-------------------------------------- | :----------- |
| id       | bigint       | 主鍵、自動遞增                          | 獨立編號     |
| user_id  | bigint       | 不可為空值，外鍵對應 user 資料表中的 id | 留言會員編號 |
| content  | varchar(255) | 不可為空值                              | 留言內容     |
| time     | datetime     | 不可為空值，預設為當前時間              | 留言時間     |

```sql
CREATE TABLE message (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  content varchar(255) NOT NULL,
  time datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO message (user_id, content)
  VALUES
  (1, "test message");
```
![4-1](/img/4-1.png)

- 使用 SELECT 搭配 JOIN 的語法，取得所有留言，資料中須包含留言會員的姓名。

```sql
SELECT message.* ,user.name
FROM message 
LEFT JOIN user
ON message.user_id=user.id;
```
![4-2](/img/4-2.png)

- 使用 SELECT 搭配 JOIN 的語法，取得 user 資料表中欄位 username 是 ply 的所有留言，資料中須包含留言會員的姓名。

```sql
SELECT message.* ,user.name
FROM message 
INNER JOIN user
ON message.user_id=user.id AND user.username='ply';
```
![4-3](/img/4-3.png)

- 透過 mysqldump 工具，將資料庫中的資料匯出到檔案 data.sql
```
mysqldump -u root -p website > data.sql

mysql -u root -p website < data.sql
```