# fastapi-docker-official
FastAPI公式のDockerを使用したチュートリアル

起動方法
1. イメージをビルド
```sh
docker build -t fastapi-app .
```

2. コンテナを起動
```sh
docker run -d -p 8080:80 --name fastapi-container fastapi-app
```

**アクセス可能なURL：**

* API: http://localhost:8080
* Swagger UI: http://localhost:8080/docs
* ReDoc: http://localhost:8080/redoc

コンテナに入るには以下のコマンドを使う。

```sh
docker exec -it fastapi-container /bin/bash
```

オプションの意味：
-i : 標準入力を開いたままにする（interactive）
-t : 疑似TTYを割り当てる（terminal）
/bin/bash : 実行するシェル
補足： slim イメージでは bash がない場合があるので、その場合は：

```sh
docker exec -it fastapi-container /bin/sh
```

アプリコンテナに入る

```sh
docker exec -it fastapi-docker-official-db-1 psql -U postgres -d fastapi_db
```

psql 基本コマンド：
|コマンド|	説明|
|----|-----|
|\dt	|テーブル一覧表示|
|\d users	|usersテーブルの構造表示|
|SELECT * FROM users;	|ユーザー一覧取得|
|\q	|psql を終了|