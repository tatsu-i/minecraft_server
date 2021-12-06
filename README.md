# minecraft server on docker

## ビルド
```
$ docker-compose build
```

## 起動方法
```
$ docker-compose up -d server
```

## ngrokの起動(ポート開放出来ない人向け)
[こちら](https://ngrok.com/)からアカウントを作成し、[Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)を取得してください。  

準備できたら環境変数にAuthtokenを設定しngrokコンテナを起動します。
```
$ export NGROK_AUTH=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ docker-compose up -d ngrok
```


## ユーザをホワイトリストで管理する
はじめにホワイトリストを有効化します。  
```
$ docker-compose exec server bash
# rcon-cli whitelist on
```
続いて接続したいアカウントをホワイトリストに追加します。  
```
# rcon-cli /whitelist add tatsui666
```
管理者権限を与えるにはOPコマンドを使います。
```
# rcon-cli /op tatsui666
```

## 通知サーバの起動
[こちら](https://notify-bot.line.me/my/)からLINEのパーソナルアクセストークンを取得します。  
取得が終わったら、トークンをコピーし`notify.json`にコピーしたトークンを記述します。  
```
$ cp notify.json.sample notify.json
$ vim notify.json
```

トークンを設定したら、通知サーバを起動します。  
```
$ docker-compose up -d notify-server
```

## サーバの表示名を変更する
```
$ sed -e 's/motd=A Vanilla Minecraft Server powered by Docker/motd=tatsui server/' -i ./mc_data/server.properties
```

## ワールドの再生成
サーバを停止しワールドを削除した後、サーバを起動します。
```
$ docker-compose stop server logstash notify-server && rm -rf mc_data/world && docker-compose up -d server && docker-compose logs -f server
```

ワールドの生成が完了したら、通知サーバを起動します。
```
$ docker-compose up -d notify-server
```
