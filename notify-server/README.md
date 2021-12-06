# 通知を送るためのAPIサーバ

## テストメッセージの送信
```
$ curl -XPOST http://localhost:8080/post/line -H 'Content-Type: application/json' -d '{"message": "test message."}'
```
