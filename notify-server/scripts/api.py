import os
import re
import sys
import json
import requests
from datetime import datetime, timedelta

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 設定読み込み
with open("/conf/notify.json") as f:
    config = json.load(f)

# LINE アクセストークン
LINE_ACCESS_TOKEN = config.get("line_access_token")


class Item(BaseModel):
    message: str


@app.post("/post/line")
def post_line(item: Item):
    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": "Bearer " + LINE_ACCESS_TOKEN}
        payload = {"message": item.message}
        requests.post(
            url,
            headers=headers,
            params=payload,
        )
    except Exception as e:
        print(e)
    return {"status": "ok"}
